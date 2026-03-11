from .service import enroll_student , get_enrollments, delete_enrollment


def enroll_student_controller(data):

    enrollment_id = enroll_student(data)

    return {
        "id": enrollment_id,
        "message": "Student enrolled successfully"
    }


def get_all_enrollments():
    return get_enrollments()

def remove_enrollment(enrollment_id):
    delete_enrollment(enrollment_id)
    return {
        "message": "Enrollment deleted successfully"
    }