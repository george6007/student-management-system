
from fastapi import FastAPI

from database import engine, Base
import database_models
from routers import students

app = FastAPI(title="Student Management System API")

# Create database tables if they do not exist
Base.metadata.create_all(bind=engine)

# Register the student router
app.include_router(students.router)


@app.get("/")
def home():
    return {"message": "Student Management System API is running!"}
