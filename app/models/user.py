from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.core.base import Base
import uuid
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, nullable=False, index = True)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable = False)
    refresh_token = Column(String(100), nullable = True)