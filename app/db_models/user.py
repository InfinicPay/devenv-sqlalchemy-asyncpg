from sqlalchemy.orm import (
    mapped_column,
    Mapped,
)
from sqlalchemy import String

from app.db import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=255))
    surname:Mapped[str] = mapped_column(String(length=255))
    email: Mapped[str] = mapped_column(String(length=255), unique=True)