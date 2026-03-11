from fastapi import FastAPI

from modules.student.router import router as student_router
from modules.subject.router import router as subject_router
from modules.enrollment.router import router as enrollment_router
from modules.professor.router import router as professor_router
from modules.career.router import router as career_router
from modules.study_plan.router import router as study_plan_router
from modules.health.router import router as health_router


app = FastAPI(
    title="University API"
)


app.include_router(student_router)
app.include_router(subject_router)
app.include_router(enrollment_router)
app.include_router(professor_router)
app.include_router(career_router)
app.include_router(study_plan_router)
app.include_router(health_router)