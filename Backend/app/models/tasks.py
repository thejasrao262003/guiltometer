from sqlalchemy import Column, String, Integer, Boolean, Date, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.models.daily_logs import DailyLog
from app.models.weekly_reports import WeeklyReport
from app.models.roadmaps import Roadmap
import uuid
from datetime import datetime, UTC, timezone
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    name = Column(String, nullable=False)
    category = Column(String)
    start_date = Column(Date, nullable=False)
    target_frequency = Column(Integer)
    expected_duration_days = Column(Integer)
    roadmap_enabled = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    description = Column(String, nullable=False)

    user = relationship("User", back_populates="tasks")
    daily_logs = relationship("DailyLog", back_populates="task", cascade="all, delete-orphan")
    weekly_reports = relationship("WeeklyReport", back_populates="task", cascade="all, delete-orphan")
    roadmaps = relationship("Roadmap", back_populates="task", cascade="all, delete-orphan")