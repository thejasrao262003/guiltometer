from pydantic import BaseModel
from uuid import UUID
from datetime import date, datetime
from typing import Optional

class RoadmapBase(BaseModel):
    week_start_date: date
    roadmap_md: str

class RoadmapCreate(RoadmapBase):
    task_id: UUID

class RoadmapUpdate(BaseModel):
    week_start_date: Optional[date] = None
    roadmap_md: Optional[str] = None

class RoadmapOut(RoadmapBase):
    id: UUID
    task_id: UUID
    created_at: datetime

    class Config:
        orm_mode = True
