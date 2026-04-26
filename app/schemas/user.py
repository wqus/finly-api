from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from uuid import UUID

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(..., max_length=6, description='Пароль минимум 6 сиимволов')

class UserUpdate(BaseModel):
    email: EmailStr | None = None
    password: str | None = Field(None, min_length=6)

class UserResponse(UserBase):
    id: UUID
    created_at: datetime

    class Config:
        from_attribues = True

class UserInDB(UserResponse):
    hashed_password: str