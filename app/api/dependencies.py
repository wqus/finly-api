from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from jose import jwt, JWTError
from app.core.config import settings
from uuid import UUID
from app.repositories.UserReposirory import UserRepository

security = HTTPBearer()

async def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security),
        db: AsyncSession = Depends(get_db)
):
    """Получить текущего пользователя по JWT токену"""
    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        user_id = payload.get('sub')
        token_type = payload.get('type')

        if token_type != 'access':
            raise HTTPException(401, "Invalid token type")
        
        if not user_id:
            raise HTTPException(401, "Invalid token")
        
        user_id = UUID(user_id)

    except JWTError:
        raise HTTPException(401, "Invalid token")
    
    user_repo = UserRepository()
    user = await user_repo.get_by_id(db, user_id)

    if not user:
        raise HTTPException(401, "User not found")
    
    return user

