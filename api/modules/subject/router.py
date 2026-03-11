from fastapi import APIRouter
from .schema import SubjectCreate, SubjectUpdate
from .controller import (
    create_subject_controller,
    get_all_subjects,
    get_subject_by_id,
    update_subject_controller,
    remove_subject
)

router = APIRouter(
    prefix="/subjects",
    tags=["Subjects"]
)


@router.post("/")
def create_subject(subject: SubjectCreate):

    return create_subject_controller(subject)


@router.get("/")
def get_subjects():

    return get_all_subjects()


@router.get("/{subject_id}")
def get_subject(subject_id: int):

    return get_subject_by_id(subject_id)


@router.put("/{subject_id}")
def update_subject(subject_id: int, subject: SubjectUpdate):

    return update_subject_controller(subject_id, subject)


@router.delete("/{subject_id}")
def delete_subject(subject_id: int):

    return remove_subject(subject_id)