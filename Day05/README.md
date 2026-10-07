# Day 5 - FastAPI Database Setup

Today I implemented the basic **database structure in FastAPI** using **SQLAlchemy, SQLite, and Pydantic**.

## Technologies Used

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## What I Implemented

### 1. Database Setup

Created `database.py` to configure the SQLite database and SQLAlchemy.

```python
Base
engine
```

The database used in this project is **SQLite**.

### 2. Database Model

Created an `Employee` model in `models/employee.py` to define the database table.

```python
class Employee(Base):
    __tablename__ = "Employees"
```

The table contains:

- `id` → Primary Key
- `name`
- `username` → Unique
- `email_id` → Unique
- `password`

### 3. Pydantic Schemas

Created schemas to validate API request and response data.

**CreateEmployee** → Used for input/request data.

```python
class CreateEmployee(BaseModel):
    name: str
    username: str
    email_id: str
    password: str
```

**EmployeeResponse** → Used to define the response data.

```python
class EmployeeResponse(BaseModel):
    id: int
    name: str
    username: str
    email_id: str
```

The password is not included in the response schema.

### 4. Main File

Created the FastAPI application in `main.py`.

```python
Base.metadata.create_all(bind=engine)
```

This creates the database tables based on the SQLAlchemy models.

Also created a basic endpoint:

```text
GET /home
```

## Database Table

```text
Employees
├── id          → Primary Key
├── name        → Required
├── username    → Unique
├── email_id    → Unique
└── passsword
```

## Project Flow

```text
FastAPI
   ↓
Database Configuration
   ↓
SQLAlchemy Model
   ↓
SQLite Table
   ↓
Pydantic Schema
   ↓
API
```

## Key Learning

Learned how to connect **FastAPI with SQLite**, create database tables using **SQLAlchemy models**, and use **Pydantic schemas** for request and response validation.