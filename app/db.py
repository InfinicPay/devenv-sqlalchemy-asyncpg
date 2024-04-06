from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import DeclarativeBase

from app.settings import settings

metadata = MetaData()


class Base(DeclarativeBase):
    pass


async_engine = create_async_engine(settings.DB_URL.unicode_string())

async def get_db():
    async with AsyncSession(async_engine) as session:
        yield session
