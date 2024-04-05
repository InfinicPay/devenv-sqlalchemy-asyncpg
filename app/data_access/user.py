
from app.pydantic_models.user import CreateUser
from sqlalchemy.ext.asyncio import AsyncSession


async def create_user(user: CreateUser, session: AsyncSession) -> None:
    try:
        user_object = CreateUser(**user.model_dump())
        session.add(user_object)
        await session.commit()
    except Exception :
        raise Exception("Problem creating user")