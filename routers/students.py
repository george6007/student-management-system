
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from schemas import StudentCreate, StudentResponse, StudentUpdate
from crud import students as student_crud

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.post("/", response_model=StudentResponse, status_code=201)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    return student_crud.create_student(db, student)


@router.get("/", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return student_crud.get_students(db)


@router.get("/{student_id}", response_model=StudentResponse)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = student_crud.get_student(db, student_id)

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


@router.put("/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student_data: StudentCreate,
    db: Session = Depends(get_db)
):
    student = student_crud.update_student(db, student_id, student_data)

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


@router.delete("/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    deleted = student_crud.delete_student(db, student_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")

    return {"message": "Student deleted successfully"}



@router.patch("/{student_id}", response_model=StudentResponse)
def patch_student(
    student_id: int,
    student_data: StudentUpdate,
    db: Session = Depends(get_db)
):
    student = student_crud.update_student_fields(
        db, student_id, student_data
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student
