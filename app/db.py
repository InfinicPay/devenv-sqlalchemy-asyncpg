from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import DeclarativeBase

from app.settings import settings

metadata = MetaData()


class Base(DeclarativeBase):
    pass


engine = create_async_engine(settings.DB_URL)

async def get_db():
    async with AsyncSession(engine) as session:
        yield session
