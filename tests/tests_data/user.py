import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from tests.dataset import USERS
from app.data_access.user import create_user, get_user


@pytest.mark.asyncio
async def test_get_user(db_session: AsyncSession):
    data = await get_user(email=USERS['user_1'].email, session=db_session)
    assert data is not None
    assert data.email == USERS["user_1"].email
