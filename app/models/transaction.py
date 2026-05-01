from sqlalchemy import Column, Numeric, Date, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.base import Base
import uuid
from sqlalchemy.sql import func


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable = False, index = True)
    wallet_id = Column(UUID(as_uuid=True), ForeignKey('wallets.id'), nullable = False, index = True)
    category_id = Column(UUID(as_uuid=True), ForeignKey('categories.id'), nullable = False, index = True)
    amount = Column(Numeric(10,2), nullable=False)
    note = Column(Text, nullable=True)
    transaction_date = Column(Date, nullable=False, server_default=func.current_date())
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    category = relationship("Category")
    wallet = relationship("Wallet")