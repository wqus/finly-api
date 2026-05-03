import os
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV = os.getenv("ENV", "dev")


class Settings(BaseSettings):
    ASYNC_DATABASE_URL: str = Field(..., alias="ASYNC_DATABASE_URL")
    SYNC_DATABASE_URL: str = Field(..., alias="SYNC_DATABASE_URL")

    SECRET_KEY: str = Field(..., alias="SECRET_KEY")
    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    model_config = SettingsConfigDict(
        env_file=".env.prod" if ENV == "prod" else ".env.dev",
        case_sensitive=True,
        extra="ignore"
    )


settings = Settings()
