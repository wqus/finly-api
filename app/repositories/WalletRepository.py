from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Wallet
from sqlalchemy import select

"""
    ⏳ get_by_id
    ⏳ get_by_user
    ⏳ create
    ⏳ update 
    ⏳ delete
    ⏳ update_balance
"""

async def get_by_id(db: AsyncSession, wallet_id: UUID) -> Wallet | None:
    result = await db.execute(select(Wallet).where(Wallet.id == wallet_id))
    return result.scalar_one_or_none()

async def get_by_id(db: AsyncSession, wallet_id: UUID) -> Wallet | None:
    result = await db.execute(select(Wallet).where(Wallet.id == wallet_id))
    return result.scalar_one_or_none()

async def get_by_id(db: AsyncSession, wallet_id: UUID) -> Wallet | None:
    result = await db.execute(select(Wallet).where(Wallet.id == wallet_id))
    return result.scalar_one_or_none()

async def get_by_id(db: AsyncSession, wallet_id: UUID) -> Wallet | None:
    result = await db.execute(select(Wallet).where(Wallet.id == wallet_id))
    return result.scalar_one_or_none()

async def get_by_id(db: AsyncSession, wallet_id: UUID) -> Wallet | None:
    result = await db.execute(select(Wallet).where(Wallet.id == wallet_id))
    return result.scalar_one_or_none()

async def get_by_id(db: AsyncSession, wallet_id: UUID) -> Wallet | None:
    result = await db.execute(select(Wallet).where(Wallet.id == wallet_id))
    return result.scalar_one_or_none()
