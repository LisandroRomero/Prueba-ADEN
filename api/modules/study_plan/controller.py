from .service import (
    create_study_plan,
    get_study_plans,
    get_study_plan,
    update_study_plan,
    delete_study_plan
)


def create_study_plan_controller(data):

    study_plan_id = create_study_plan(data)

    return {
        "id": study_plan_id,
        "message": "Study plan created successfully"
    }


def get_all_study_plans():

    return get_study_plans()


def get_study_plan_by_id(study_plan_id):

    return get_study_plan(study_plan_id)


def update_study_plan_controller(study_plan_id, data):

    update_study_plan(study_plan_id, data)

    return {
        "message": "Study plan updated successfully"
    }


def remove_study_plan(study_plan_id):

    return delete_study_plan(study_plan_id)