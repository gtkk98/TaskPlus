from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: str
    is_completed: bool = False
    
class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    
# This tells Pydantic to read data even if it's not a standard dictionary 
# (SQLAlchemy models are objects, not dicts)
    class Config:
        from_attributes: True    