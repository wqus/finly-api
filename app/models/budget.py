from sqlalchemy import Column, Numeric, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base
import uuid

class Budget(Base):
    __tablename__ = 'budgets'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False, index = True)
    category_id = Column(UUID(as_uuid= True), ForeignKey("categories.id"), nullable = False, index = True)
    month = Column(Date, nullable = False)
    limit_amount = Column(Numeric(10,2), nullable=False)

    category = relationship("Category")