import os
from urllib import parse
from pydantic import PositiveInt, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "test-api"
    APP_VERSION: str = "1"
    DESCRIPTION: str = "app for bug replication"
    HOST: str = os.getenv("DEV_HOST", "127.0.0.1")
    PORT: PositiveInt = int(os.getenv("DEV_PORT", "8008"))
    FASTAPI_CORS_ORIGINS: str = os.getenv("FASTAPI_CORS_ORIGINS", "").split(",")
    DB_URL: PostgresDsn = (
        "postgresql+asyncpg://postgres@localhost:5432/test-db"
    )

settings = Settings()