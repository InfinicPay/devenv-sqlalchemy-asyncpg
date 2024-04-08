from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import EmailStr
from typing import Optional
from app.settings import settings
from app.pydantic_models.user import CreateUser
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app.data_access.user import create_user, get_user


router = APIRouter(prefix=f"/v{settings.APP_VERSION}", tags=["users"])


@router.post("/user",)
async def post_user(
    user: CreateUser, session: AsyncSession = Depends(get_db)
) -> CreateUser:
    try:
        await create_user(user=user, session=session)
        return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail=f"There was a problem creating user")
    


@router.get("/users",)
async def get_users(
    email: EmailStr | None = None, session: AsyncSession = Depends(get_db)
) -> list:
    try:
        if email:
            result = await get_user(email=email, session=session)
        else:
            result = await get_user(session=session)
        if result:
            return result
        return []
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail=f"There was a problem retrieving users")