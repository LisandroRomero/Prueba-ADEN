from fastapi import APIRouter
from .schema import EnrollmentCreate
from .controller import enroll_student_controller, get_all_enrollments, remove_enrollment

router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"]
)


@router.post("/")
def enroll_student(enrollment: EnrollmentCreate):

    return enroll_student_controller(enrollment)


@router.get("/")
def get_enrollments():
    return get_all_enrollments()

@router.delete("/{enrollment_id}")
def delete_enrollment(enrollment_id:int):
    return remove_enrollment(enrollment_id)