from core.odoo_client import OdooClient

odoo = OdooClient()


def enroll_student(data):

    enrollment_id = odoo.execute(
        "university.enrollment",
        "create",
        [{
            "student_id": data.student_id,
            "subject_id": data.subject_id
        }]
    )

    return enrollment_id


def get_enrollments():

    return odoo.execute(
        "university.enrollment",
        "search_read",
        [],
        {"fields": ["id", "student_id", "subject_id", "date"]}
    )


def delete_enrollment(enrollment_id):

    return odoo.execute(
        "university.enrollment",
        "unlink",
        [enrollment_id]
    )