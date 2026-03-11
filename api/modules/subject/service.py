from core.odoo_client import OdooClient

odoo = OdooClient()


def create_subject(data):

    subject_id = odoo.execute(
        "university.subject",
        "create",
        [{
            "name": data.name,
            "max_capacity": data.max_capacity,
            "professor_id": data.professor_id,
            "study_plan_id": data.study_plan_id
        }]
    )

    return subject_id

def get_subjects():

    return odoo.execute(
        "university.subject",
        "search_read",
        [],
        {"fields": ["id", "name", "max_capacity", "professor_id"]}
    )

def get_subjects():

    return odoo.execute(
        "university.subject",
        "search_read",
        [],
        {
            "fields": [
                "id",
                "name",
                "max_capacity",
                "student_count",
                "professor_id",
                "study_plan_id"
            ]
        }
    )


def get_subject(subject_id):

    result = odoo.execute(
        "university.subject",
        "read",
        [[subject_id]],
        {
            "fields": [
                "id",
                "name",
                "max_capacity",
                "student_count",
                "professor_id",
                "study_plan_id"
            ]
        }
    )

    return result


def update_subject(subject_id, data):

    return odoo.execute(
        "university.subject",
        "write",
        [[subject_id], data.dict(exclude_none=True)]
    )


def delete_subject(subject_id):

    return odoo.execute(
        "university.subject",
        "unlink",
        [subject_id]
    )