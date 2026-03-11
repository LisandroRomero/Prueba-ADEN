from fastapi import APIRouter
from .schema import ProfessorCreate, ProfessorUpdate
from .controller import (
    create_professor_controller,
    get_all_professors,
    get_professor_by_id,
    update_professor_controller,
    remove_professor
)

router = APIRouter(
    prefix="/professors",
    tags=["Professors"]
)


@router.post("/")
def create_professor(professor: ProfessorCreate):
    return create_professor_controller(professor)


@router.get("/")
def get_professors():
    return get_all_professors()


@router.get("/{professor_id}")
def get_professor(professor_id: int):
    return get_professor_by_id(professor_id)


@router.put("/{professor_id}")
def update_professor(professor_id: int, professor: ProfessorUpdate):
    return update_professor_controller(professor_id, professor)


@router.delete("/{professor_id}")
def delete_professor(professor_id: int):
    return remove_professor(professor_id)