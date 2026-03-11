from core.odoo_client import OdooClient

odoo = OdooClient()


def create_career(data):

    career_id = odoo.execute(
        "university.career",
        "create",
        [{
            "name": data.name
        }]
    )

    return career_id


def get_careers():

    return odoo.execute(
        "university.career",
        "search_read",
        [],
        {"fields": ["id", "name"]}
    )


def get_career(career_id):

    return odoo.execute(
        "university.career",
        "read",
        [[career_id]],
        {"fields": ["id", "name"]}
    )


def update_career(career_id, data):

    return odoo.execute(
        "university.career",
        "write",
        [[career_id], data.dict(exclude_none=True)]
    )


def delete_career(career_id):

    return odoo.execute(
        "university.career",
        "unlink",
        [career_id]
    )