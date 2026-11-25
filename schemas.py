
from pydantic import BaseModel, EmailStr


class StudentCreate(BaseModel):
    name: str
    age: int
    email: EmailStr
    course: str

class StudentUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    email: EmailStr | None = None
    course: str | None = None


class StudentResponse(StudentCreate):
    id: int

    class Config:
        from_attributes = True
