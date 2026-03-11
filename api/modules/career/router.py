from fastapi import APIRouter
from .schema import CareerCreate, CareerUpdate
from .controller import (
    create_career_controller,
    get_all_careers,
    get_career_by_id,
    update_career_controller,
    remove_career
)

router = APIRouter(
    prefix="/careers",
    tags=["Careers"]
)


@router.post("/")
def create_career(career: CareerCreate):

    return create_career_controller(career)


@router.get("/")
def get_careers():

    return get_all_careers()


@router.get("/{career_id}")
def get_career(career_id: int):

    return get_career_by_id(career_id)


@router.put("/{career_id}")
def update_career(career_id: int, career: CareerUpdate):

    return update_career_controller(career_id, career)


@router.delete("/{career_id}")
def delete_career(career_id: int):

    return remove_career(career_id)