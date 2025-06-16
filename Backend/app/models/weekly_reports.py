from sqlalchemy import Column, Integer, Date, ForeignKey, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
# from app.models.tasks import Task
import uuid
from datetime import datetime, UTC, timezone
from app.database import Base

class WeeklyReport(Base):

    __tablename__ = "weekly_reports"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    task_id = Column(UUID(as_uuid=True), ForeignKey("tasks.id", ondelete="CASCADE"), nullable=False)
    week_start_date = Column(Date, nullable=False)
    guilt_score = Column(Integer)
    analysis = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    task = relationship("Task", back_populates="weekly_reports")