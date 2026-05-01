from uuid import UUID
from pydantic import BaseModel
from app.schemas.transaction import TransactionType

class CategoryCreate(BaseModel):
    name: str
    type: TransactionType 

class CategoryResponse(BaseModel):
    id: UUID
    user_id: UUID
    name: str
    type: TransactionType 
    
    class Config:
        from_attributes = True