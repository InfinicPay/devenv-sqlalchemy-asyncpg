import asyncio

import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.settings import settings
from app.db import Base
from tests.dataset import USERS

# Normally we would use a test db separate from the main db but, this repois just for bug reproduction
DATABASE_URL = settings.DB_URL


@pytest_asyncio.fixture(scope="session")
def db_sessionmaker():
    db_engine = create_async_engine(
        DATABASE_URL,
        echo=False,
    )
    db_sessionmaker = sessionmaker(
        bind=db_engine,
        expire_on_commit=False,
        class_=AsyncSession,
    )

    async def init_models():
        async with db_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    asyncio.run(init_models())
    yield db_sessionmaker


@pytest_asyncio.fixture(scope="session")
async def db_session(
    db_sessionmaker,
):
    async with db_sessionmaker() as session:
        for table in reversed(Base.metadata.sorted_tables):
            # Clear DB after every test
            await session.execute(table.delete())
            await session.commit()
        yield session


class SetUpDB:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def test_dataset(self):
        for each_user in USERS.values():
            self.db_session.add(each_user)
        await self.db_session.commit()



@pytest_asyncio.fixture(scope="session", autouse=True)
async def data_set(db_session: AsyncSession):
    setup_db = SetUpDB(db_session=db_session)
    await setup_db.test_dataset()
