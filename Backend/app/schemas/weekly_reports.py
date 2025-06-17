from pydantic import BaseModel
from uuid import UUID
from datetime import date, datetime
from typing import Optional

class WeeklyReportBase(BaseModel):
    week_start_date: date
    guilt_score: Optional[int] = None
    analysis: str

class WeeklyReportCreate(WeeklyReportBase):
    task_id: UUID

class WeeklyReportUpdate(BaseModel):
    week_start_date: Optional[date] = None
    guilt_score: Optional[int] = None
    analysis: Optional[str] = None

class WeeklyReportOut(WeeklyReportBase):
    id: UUID
    task_id: UUID
    created_at: datetime

    class Config:
        orm_mode = True
