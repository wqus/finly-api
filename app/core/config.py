from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # Database
    ASYNC_DATABASE_URL: str = Field(..., alias="ASYNC_DATABASE_URL")
    SYNC_DATABASE_URL: str = Field(..., alias="SYNC_DATABASE_URL")
    
    # JWT
    SECRET_KEY: str = Field(..., alias="SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()

import os
ENV = os.getenv("ENV", "dev")

if ENV == "prod":
    settings = Settings(_env_file=".env.prod")
else:
    settings = Settings(_env_file=".env.test")
