from sqlalchemy import Column, String, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.core.base import Base
import uuid

class Wallet(Base):
    __tablename__ = 'wallets'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False, index = True)
    name = Column(String(100), nullable=False)
    balance = Column(Numeric(10,2), nullable=False, default=0)
    