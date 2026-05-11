from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.wallet import Wallet
from sqlalchemy import select
from decimal import Decimal


class WalletRepository:
    async def get_by_id(self, db: AsyncSession, wallet_id: UUID, user_id: UUID) -> Wallet | None:
        result = await db.execute(select(Wallet).where(Wallet.id == wallet_id, Wallet.user_id == user_id))
        return result.scalar_one_or_none()

    async def get_by_user(self, db: AsyncSession, user_id: UUID) -> list:
        result = await db.execute(select(Wallet).where(Wallet.user_id == user_id))
        return result.scalars().all()

    async def create(self, db: AsyncSession, user_id: UUID, name: str, balance: Decimal  = Decimal(0)) -> Wallet | None:
        wallet = Wallet(user_id = user_id, balance = balance, name = name)
        db.add(wallet)

        await db.commit()
        await db.refresh(wallet)

        return wallet

    async def update(self, db: AsyncSession, wallet: Wallet) -> Wallet:
        await db.commit()
        await db.refresh(wallet)
        
        return wallet

    async def delete(self, db: AsyncSession, wallet_id: UUID, user_id) -> bool:
        wallet = await db.get(Wallet, wallet_id)
        if wallet and wallet.user_id == user_id:
           await db.delete(wallet)
           await db.commit()
           return True
        return False
    

    async def update_balance(self, db: AsyncSession, wallet_id: UUID, amount: Decimal, transaction_type: str) -> Wallet | None:
        wallet = await db.get(Wallet, wallet_id)
        if not wallet:
            return None
        if transaction_type == 'income':
            wallet.balance += amount
        elif transaction_type == 'expense':
            wallet.balance -= amount
        else: return wallet
        
        await db.commit()
        await db.refresh(wallet)
        return wallet
