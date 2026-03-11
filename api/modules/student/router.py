from fastapi import APIRouter
from .schema import StudentCreate
from .controller import create_student_controller, get_all_students, get_student_by_id, remove_student, update_student_controller

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.post("/")
def create_student(student: StudentCreate):

    student_id = create_student_controller(student)

    return {
        "id": student_id,
        "message": "Student created"
    }
    
@router.get("/")
def get_students():
    return get_all_students()

@router.get("/{student_id}")
def get_student(student_id: int):
    return get_student_by_id(student_id)


@router.put("/{student_id}")
def update_student(student_id: int, student: StudentCreate):
    return update_student_controller(student_id, student)


@router.delete("/{student_id}")
def delete_student(student_id: int):
    return remove_student(student_id)