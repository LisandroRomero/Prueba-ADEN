from typing import Optional
from pydantic import BaseModel


class StudentCreate(BaseModel):
    name: str
    email: str
    phone: int