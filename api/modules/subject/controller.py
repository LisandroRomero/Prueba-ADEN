from .service import (
    create_subject,
    get_subjects,
    get_subject,
    update_subject,
    delete_subject
)


def create_subject_controller(data):

    subject_id = create_subject(data)

    return {
        "id": subject_id,
        "message": "Subject created successfully"
    }


def get_all_subjects():

    return get_subjects()


def get_subject_by_id(subject_id):

    return get_subject(subject_id)


def update_subject_controller(subject_id, data):

    update_subject(subject_id, data)

    return {
        "message": "Subject updated successfully"
    }


def remove_subject(subject_id):

    return delete_subject(subject_id)