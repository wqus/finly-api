from pydantic import BaseModel, Field, field_validator
from datetime import datetime, date
from uuid import UUID
from decimal import Decimal
from enum import Enum

class TransactionType(str, Enum):
    INCOME = 'income'
    EXPENSE = 'expense'

class TransactionBase(BaseModel):
    wallet_id: UUID
    category_id: UUID
    amount: Decimal = Field(..., gt = 0, decimal_places=2)
    type: TransactionnType
    note: str | None = Field(None, max_length=500)
    transaction_date: date = Field(default_factory=date.today)

    
class TransactionUpdate(BaseModel):
    wallet_id: UUID | None = None
    category_id: UUID | None = None
    amount: Decimal | None =  Field(None, gt = 0, decimal_places=2)
    type: TransactionnType | None = None
    note: str | None = None
    transaction_date: date | None = None

class TransactionResponse(TransactionBase):
    id: UUID
    user_id: UUID
    category_name: str  
    created_at: datetime
    
    class Config:
        from_attributes = True