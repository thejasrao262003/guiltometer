from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from uuid import UUID
from datetime import date, datetime

class DailyLogBase(BaseModel):
    date: date
    metrics: Dict[str, Any]
    note: Optional[str] = None

class DailyLogCreate(DailyLogBase):
    task_id: UUID

class DailyLogUpdate(BaseModel):
    date: Optional[date] = None
    metrics: Optional[Dict[str, Any]] = None
    note: Optional[str] = None

class DailyLogOut(DailyLogBase):
    id: UUID
    task_id: UUID
    created_at: datetime

    class Config:
        orm_mode = True
