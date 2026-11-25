
# Student Management System

A REST API built using **FastAPI** and **PostgreSQL** to manage student records.

## Technologies Used
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic

## Features
- Add a student
- View all students
- View a student by ID
- Update student details
- Partially update student fields
- Delete a student

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/george6007/student-management-system.git
   cd student-management-system
   ```

2. Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure your PostgreSQL database and database connection settings.

5. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

## API Documentation

Open http://127.0.0.1:8000/docs to test the API using Swagger UI.

## Author

George Jacob
