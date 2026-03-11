from typing import Optional
from pydantic import BaseModel


class SubjectCreate(BaseModel):
    name: str
    max_capacity: int
    professor_id: Optional[int] = None
    study_plan_id: Optional[int] = None


class SubjectUpdate(BaseModel):
    name: str | None = None
    max_capacity: int | None = None
    professor_id: int | None = None
    study_plan_id: int | None = None