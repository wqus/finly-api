from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from sqlalchemy import select

class UserRepository:
    async def get_by_id(self, db: AsyncSession, user_id: UUID) -> User | None:
        result = await db.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()
    
    async def get_by_email(self, db: AsyncSession, email: str) -> User | None:
        result = await db.execute(select(User).where(User.email  == email))
        return result.scalar_one_or_none()
    
    async def create(self, db: AsyncSession, email: str, hashed_password: str) -> User:
        user = User(
            email = email,
            hashed_password = hashed_password
        )
        db.add(user)

        await db.commit()

        await db.refresh(user)

        return user
    
    async def update(self, db: AsyncSession, user: User) -> User:
        await db.commit()
        await db.refresh(user)
        
        return user
    
    async def delete(self, db: AsyncSession, user_id: UUID) -> bool:
        user = await db.get(User, user_id)
        if user and user.id == user_id:
           await db.delete(user)
           await db.commit()
           return True
        return False
    
    async def update_refresh_token(self, db: AsyncSession, user_id: UUID, refresh_token: str | None) -> User | None:
        user = await db.get(User, user_id)
        if user:
            user.refresh_token = refresh_token
            await db.commit()
            await db.refresh(user)
        return user