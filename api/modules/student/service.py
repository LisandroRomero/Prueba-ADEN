from core.odoo_client import OdooClient

odoo = OdooClient()


def create_student(data):

    student_id = odoo.execute(
        "university.student",
        "create",
        [{
            "name": data.name,
            "email": data.email
        }]
    )

    return student_id


def get_students():

    return odoo.execute(
        "university.student",
        "search_read",
        [[]],
        {"fields": ["id", "name", "email", "phone"]}
    )

def get_student(student_id):

    student = odoo.execute(
        "university.student",
        "read",
        [student_id],
        {"fields": ["id", "name", "email", "phone"]}
    )

    return student

def update_student(student_id, data):

    return odoo.execute(
        "university.student",
        "write",
        [[student_id], {
            "name": data.name,
            "email": data.email,
            "phone": data.phone
        }]
    )


def delete_student(student_id):

    return odoo.execute(
        "university.student",
        "unlink",
        [student_id]
    )