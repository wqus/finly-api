# app/services/wallet_service.py
from uuid import UUID
from decimal import Decimal
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from app.repositories.WalletRepository import WalletRepository
from app.schemas.wallet import WalletCreate, WalletUpdate, WalletResponse

class WalletService:
    def __init__(self, wallet_repo: WalletRepository):
        self.wallet_repo = wallet_repo

    async def get_user_wallets(): 
        wallets = await self.wallet_repo.get_by_id()
    async def get_wallet_by_id(): pass
    async def create_wallet(): pass
    async def update_wallet(): pass
    async def delete_wallet(): pass
    async def update_balance(): pass
