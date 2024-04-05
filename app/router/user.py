from fastapi import APIRouter, Depends, Request, HTTPException, status
from app.settings import settings
from app.pydantic_models.user import CreateUser
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app.data_access.user import create_user


router = APIRouter(prefix=f"/v{settings.APP_VERSION}", tags=["users"])


@router.post(
    "/user",
)
async def post_user(
    request: Request, user: CreateUser, session: AsyncSession = Depends(get_db)
) -> CreateUser:
    try:
        user = await create_user(user=user, session=session)
        return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="There was a problem creating user")