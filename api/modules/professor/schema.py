from pydantic import BaseModel


class ProfessorCreate(BaseModel):
    name: str
    email: str | None = None


class ProfessorUpdate(BaseModel):
    name: str | None = None
    email: str | None = None