from .service import create_student, delete_student, get_student, get_students, update_student


def create_student_controller(data):

    student_id = create_student(data)

    return {
        "id": student_id,
        "message": "Student created successfully"
    }

def get_all_students():
    return get_students()


def get_student_by_id(student_id):
    return get_student(student_id)


def update_student_controller(student_id, data):

    update_student(student_id, data)

    return {
        "message": "Student updated successfully"
    }


def remove_student(student_id):

    delete_student(student_id)

    return {
        "message": "Student deleted successfully"
    }
    