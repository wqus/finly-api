from pydantic import BaseModel, Field
from uuid import UUID
from decimal import Decimal


class WalletCreate(BaseModel):
    name: str = Field(..., max_length=100)
    balance: Decimal = Field(0, ge=0)

class WalletUpdate(BaseModel):
    name: str | None = Field(None, max_length=100)
    balance: Decimal | None = Field(None , ge = 0)

class WalletResponse(BaseModel):
    id: UUID
    user_id: UUID
    name: str
    balance: Decimal

    class Config:
        from_attributes = True

