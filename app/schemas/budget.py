from pydantic import BaseModel, Field
from uuid import UUID
from decimal import Decimal
from datetime import date

class BudgetBase(BaseModel):
    category_id: UUID
    month: date 
    limit_amount: Decimal = Field(..., gt=0, decimal_places=2)

class BudgetResponse(BudgetBase):
    id: UUID
    user_id: UUID
    spent_amount: Decimal | None = None
    
    class Config:
        from_attributes = True