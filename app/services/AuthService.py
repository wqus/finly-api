from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from uuid import UUID
from fastapi import HTTPException
from app.models.user import User
from app.repositories.UserReposirory import UserRepository
from app.core.config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    def hash_password(self, password: str) -> str:
        """Хеширует пароль"""
        print(f"Длина пароля: {len(password)}")
        print(f"Тип: {type(password)}")
        return pwd_context.hash(password)
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Проверяет пароль"""
        return pwd_context.verify(plain_password, hashed_password) 
      
    def create_access_token(self, user_id) -> str:
        """Создаёт access_token (живёт 30 минут)"""
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        payload = {
            'sub': str(user_id),
            'exp': expire,
            'type': 'access'
        }

        return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    
    def create_refresh_token(self, user_id) -> str:
        """Создаёт refresh_token (живёт 7 дней)"""
        expire = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        payload = {
            "sub": str(user_id),
            "exp": expire,
            "type": "refresh"
        }
        return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    
    async def register(self, db: AsyncSession, email: str, password: str) -> dict:
        "Регистрация нового пользователя"
        existing = await self.user_repo.get_by_email(db, email)
        if existing:
            raise HTTPException(409, "Email already exists")
        hashed = self.hash_password(password)
        print(hashed)
        user = await self.user_repo.create(db, email, hashed)
        access_token = self.create_access_token(user.id)
        refresh_token = self.create_refresh_token(user.id)

        await self.user_repo.update_refresh_token(db, user.id, refresh_token)

        return {
            'user': user,
            'access_token': access_token,
            'refresh_token': refresh_token
        }
    
    async def login(self, db,  email: str, password: str) -> dict:
        """Логин пользователя"""
        user = await self.user_repo.get_by_email(db, email)
        if not user:
            raise HTTPException(409, 'Invalid credentials')
        
        if not self.verify_password(password, user.hashed_password):
            raise HTTPException(409, 'Invalid credentials')
        
        access_token = self.create_access_token(user.id)
        refresh_token = self.create_refresh_token(user.id)
        
        await self.user_repo.update_refresh_token(db, user.id, refresh_token)
        
        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }


    async def update_user(self, current_user: User, db: AsyncSession, data: dict) -> User:
        if data.email:
            existing = await self.user_repo.get_by_email(db, data.email)
            if existing and existing.id != current_user.id:
                raise HTTPException(409, 'Email already exists') 
            current_user.email = data.email
    
        if data.password:
            current_user.hashed_password = self.hash_password(data.password)

        await self.user_repo.update(db, current_user)
        return current_user
        
    async def refresh_token(self, db, refresh_token: str) -> dict:
        """Обновление access_token по refresh_token"""
    
        try:
            payload = jwt.decode(
                refresh_token,
                settings.SECRET_KEY,
                algorithms=[settings.ALGORITHM]
            )

            user_id = payload.get("sub")
            token_type = payload.get("type")

            if token_type != "refresh":
                raise HTTPException(401, "Invalid token type")
            
            if not user_id:
                raise HTTPException(401, "Invalid token")
        except JWTError:
            raise HTTPException(401, "Invalid token")

        user = await self.user_repo.get_by_id(db, user_id)  
        if not user or user.refresh_token != refresh_token:
            raise HTTPException(401, "Invalid refresh token")

        new_access_token = self.create_access_token(user_id)

        return {
            "access_token": new_access_token,
            "refresh_token": refresh_token
        }
    async def logout(self, db, user_id) -> None:
        await self.user_repo.update_refresh_token(db, user_id, None)
        
    async def delete_user(self, db: AsyncSession, user_id: UUID) -> bool:
        return await self.user_repo.delete(db , user_id)
        