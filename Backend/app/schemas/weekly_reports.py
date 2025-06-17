from pydantic import BaseModel
from uuid import UUID
from datetime import date, datetime
from typing import Optional, Dict, Any

class WeeklyReportBase(BaseModel):
    week_start_date: date
    metrics: Dict[str, Any]  # Flexible dynamic metrics
    analysis: str

class WeeklyReportCreate(WeeklyReportBase):
    task_id: UUID

class WeeklyReportUpdate(BaseModel):
    week_start_date: Optional[date] = None
    metrics: Optional[Dict[str, Any]] = None
    analysis: Optional[str] = None

class WeeklyReportOut(WeeklyReportBase):
    id: UUID
    task_id: UUID
    created_at: datetime

    class Config:
        orm_mode = True
