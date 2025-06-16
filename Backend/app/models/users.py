from sqlalchemy import Column, String, Integer, Float, Boolean, Date, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship, declarative_base
from app.models.tasks import Task
import uuid
from datetime import datetime, UTC, timezone
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    api_key = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    encrypted_password = Column(Text, nullable=False)

    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")
    