from sqlalchemy import Column, Integer, Date, ForeignKey, Text, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime, UTC
from app.database import Base

class Roadmap(Base):
    __tablename__ = "roadmaps"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    task_id = Column(UUID(as_uuid=True), ForeignKey("tasks.id", ondelete="CASCADE"), nullable=False)
    week_start_date = Column(Date, nullable=False)
    roadmap_md = Column(Text, nullable=False)
    created_at = Column(Date, default=lambda: datetime.now(UTC))

    task = relationship("Task", back_populates="roadmaps")