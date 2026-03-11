from .service import (
    create_professor,
    get_professors,
    get_professor,
    update_professor,
    delete_professor
)


def create_professor_controller(data):

    professor_id = create_professor(data)

    return {
        "id": professor_id,
        "message": "Professor created successfully"
    }


def get_all_professors():
    return get_professors()


def get_professor_by_id(professor_id):
    return get_professor(professor_id)


def update_professor_controller(professor_id, data):

    update_professor(professor_id, data)

    return {
        "message": "Professor updated successfully"
    }


def remove_professor(professor_id):
    return delete_professor(professor_id)