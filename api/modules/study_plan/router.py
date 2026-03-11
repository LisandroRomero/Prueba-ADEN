from fastapi import APIRouter
from .schema import StudyPlanCreate, StudyPlanUpdate
from .controller import (
    create_study_plan_controller,
    get_all_study_plans,
    get_study_plan_by_id,
    update_study_plan_controller,
    remove_study_plan
)

router = APIRouter(
    prefix="/study-plans",
    tags=["Study Plans"]
)


@router.post("/")
def create_study_plan(plan: StudyPlanCreate):

    return create_study_plan_controller(plan)


@router.get("/")
def get_study_plans():

    return get_all_study_plans()


@router.get("/{plan_id}")
def get_study_plan(plan_id: int):

    return get_study_plan_by_id(plan_id)


@router.put("/{plan_id}")
def update_study_plan(plan_id: int, plan: StudyPlanUpdate):

    return update_study_plan_controller(plan_id, plan)


@router.delete("/{plan_id}")
def delete_study_plan(plan_id: int):

    return remove_study_plan(plan_id)