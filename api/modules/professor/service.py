from core.odoo_client import OdooClient

odoo = OdooClient()


def create_professor(data):

    professor_id = odoo.execute(
        "university.professor",
        "create",
        [{
            "name": data.name,
            "email": data.email
        }]
    )

    return professor_id


def get_professors():

    return odoo.execute(
        "university.professor",
        "search_read",
        [],
        {"fields": ["id", "name", "email"]}
    )


def get_professor(professor_id):

    return odoo.execute(
        "university.professor",
        "read",
        [[professor_id]],
        {"fields": ["id", "name", "email"]}
    )


def update_professor(professor_id, data):

    return odoo.execute(
        "university.professor",
        "write",
        [[professor_id], data.dict(exclude_none=True)]
    )


def delete_professor(professor_id):

    return odoo.execute(
        "university.professor",
        "unlink",
        [professor_id]
    )