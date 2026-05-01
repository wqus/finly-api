from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from uuid import UUID

class PeriodRequest(BaseModel):
    start_date: date
    end_date: date

class ExpensesByCategory(BaseModel):
    category_id: UUID
    category_name: str
    total_amount: Decimal

class BudgetAlert(BaseModel):
    category_name: str
    limit_amount: Decimal
    spent_amount: Decimal
    percentage: float
    is_exceeded: bool