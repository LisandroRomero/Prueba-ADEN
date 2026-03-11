from pydantic import BaseModel


class StudyPlanCreate(BaseModel):
    name: str
    career_id: int


class StudyPlanUpdate(BaseModel):
    name: str | None = None
    career_id: int | None = None