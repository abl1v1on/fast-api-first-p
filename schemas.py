from typing import Optional
from pydantic import BaseModel, ConfigDict


class TaskAdd(BaseModel):
    name: str
    desc: Optional[str] = None # Необязательное поле


class Task(TaskAdd):
    id: int
