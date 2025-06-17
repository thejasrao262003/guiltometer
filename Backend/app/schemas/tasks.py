from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional
class TaskCreate(BaseModel):
    name : str
    category : str
    start_date : date
    target_frequency: int
    expected_duration_days : int
    roadmap_enabled : bool
    description : str

class TaskUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    start_date: Optional[date] = None
    target_frequency: Optional[int] = None
    expected_duration_days: Optional[int] = None
    roadmap_enabled: Optional[bool] = None
    description: Optional[str] = None

