
from pydantic import EmailStr

from app.db_models.user import User
from app.pydantic_models.user import CreateUser

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def create_user(user: CreateUser, session: AsyncSession) -> None:
    try:
        user_object = User(**user.model_dump())
        session.add(user_object)
        await session.commit()
    except Exception:
        raise Exception
    


async def get_user(
    session: AsyncSession,
    email: EmailStr | None = None,
) -> User | None:
    
    query_stmnt = select(User)
    if email:
        query_stmnt = select(User).where(User.email == email)
    result = (await session.execute(query_stmnt)).scalars().all()
    print(result)
    response = list()
    if result:
        for row in result:
            user_to_append = CreateUser(email=row.email, name=row.name, surname=row.surname)
            response.append(user_to_append)
        return response
    return None