from pydantic import BaseModel, Field
from datetime import datetime


class TaskCreate(BaseModel):
    title: str = Field(max_length=100)
    description: str | None = Field(None, max_length=256)


class TaskUpdate(BaseModel):
    title: str | None = Field(None, max_length=100)
    description: str | None = Field(None, max_length=256)
    completed: bool | None = None


class TaskResponse(BaseModel):
    id: int
    title: str = Field(max_length=100)
    description: str | None = Field(None, max_length=256)
    completed: bool
    created_at: datetime
    model_config = {"from_attributes": True}
