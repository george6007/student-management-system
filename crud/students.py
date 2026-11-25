
from sqlalchemy.orm import Session
from database_models import Student
from schemas import StudentCreate


def create_student(db: Session, student: StudentCreate):
    db_student = Student(
        name=student.name,
        age=student.age,
        email=str(student.email),
        course=student.course
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


def get_students(db: Session):
    return db.query(Student).all()


def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()


def update_student(db: Session, student_id: int, student: StudentCreate):
    db_student = get_student(db, student_id)

    if db_student is None:
        return None

    db_student.name = student.name
    db_student.age = student.age
    db_student.email = str(student.email)
    db_student.course = student.course

    db.commit()
    db.refresh(db_student)

    return db_student


def delete_student(db: Session, student_id: int):
    db_student = get_student(db, student_id)

    if db_student is None:
        return False

    db.delete(db_student)
    db.commit()

    return True



from schemas import StudentCreate, StudentUpdate

def update_student_fields(
    db: Session,
    student_id: int,
    student_data: StudentUpdate
):
    db_student = get_student(db, student_id)

    if db_student is None:
        return None

    update_data = student_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_student, field, value)

    db.commit()
    db.refresh(db_student)

    return db_student
