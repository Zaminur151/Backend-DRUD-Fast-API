from datetime import datetime
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str = ""
    completed: bool = False

class TaskOut(TaskCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True