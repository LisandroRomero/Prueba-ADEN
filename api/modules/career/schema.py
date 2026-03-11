from pydantic import BaseModel


class CareerCreate(BaseModel):
    name: str


class CareerUpdate(BaseModel):
    name: str | None = None