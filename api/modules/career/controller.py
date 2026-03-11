from .service import (
    create_career,
    get_careers,
    get_career,
    update_career,
    delete_career
)


def create_career_controller(data):

    career_id = create_career(data)

    return {
        "id": career_id,
        "message": "Career created successfully"
    }


def get_all_careers():

    return get_careers()


def get_career_by_id(career_id):

    return get_career(career_id)


def update_career_controller(career_id, data):

    update_career(career_id, data)

    return {
        "message": "Career updated successfully"
    }


def remove_career(career_id):

    return delete_career(career_id)