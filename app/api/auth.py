from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.schemas.auth import LoginRequest, TokenResponse, RefreshRequest
from app.services.AuthService import AuthService
from app.api.dependencies import get_current_user

router = APIRouter(prefix="/auth", tags = ["Authentcation"])

@router.post("/register", response_model= UserResponse, status_code=201)
async def register(
    data: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    """Регистрация нового пользователя"""
    auth_service = AuthService()
    result = await auth_service.register(db, data.email, data.password)
    return result["user"]

@router.post("/login", response_model = TokenResponse)
async def login(
    data: LoginRequest,
    db: AsyncSession = Depends(get_db)
):
    """Вход в систему"""
    auth_service = AuthService()
    tokens = await auth_service.login(email=data.email, password=data.password)
    return tokens

@router.post("/refresh", response_model=TokenResponse)
async def refresh(
    data: RefreshRequest,
    db: AsyncSession = Depends(get_db)
):
    """Обновление access_token по refresh_token"""
    auth_service = AuthService()
    tokens = await auth_service.refresh_token(db, data.refresh_token)
    return tokens


@router.post("/logout", status_code=204)
async def logout(
    current_user = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Выход из системы (удаляет refresh_token)"""
    auth_service = AuthService()
    await auth_service.logout(db, current_user.id)
    return None