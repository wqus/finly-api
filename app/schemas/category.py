from uuid import UUID
from pydantic import BaseModel
from app.schemas.transaction import TransactionType

class CategoryCreate(BaseModel):
    name: str
    type: TransactionType  # ← тип: доходная это категория или расходная

class CategoryResponse(BaseModel):
    id: UUID
    user_id: UUID
    name: str
    type: TransactionType  # ← показываем клиенту тип категории
    
    class Config:
        from_attributes = True