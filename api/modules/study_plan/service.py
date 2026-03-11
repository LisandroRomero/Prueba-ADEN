from core.odoo_client import OdooClient

odoo = OdooClient()


def create_study_plan(data):

    study_plan_id = odoo.execute(
        "university.study_plan",
        "create",
        [{
            "name": data.name,
            "career_id": data.career_id
        }]
    )

    return study_plan_id


def get_study_plans():

    return odoo.execute(
        "university.study_plan",
        "search_read",
        [],
        {"fields": ["id", "name", "career_id"]}
    )


def get_study_plan(study_plan_id):

    result = odoo.execute(
        "university.study_plan",
        "read",
        [[study_plan_id]],
        {"fields": ["id", "name", "career_id"]}
    )

    return result


def update_study_plan(study_plan_id, data):

    return odoo.execute(
        "university.study_plan",
        "write",
        [[study_plan_id], data.dict(exclude_none=True)]
    )


def delete_study_plan(study_plan_id):

    return odoo.execute(
        "university.study_plan",
        "unlink",
        [study_plan_id]
    )