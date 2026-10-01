# FastAPI Employee API

A simple Employee API built using **FastAPI** and **Pydantic** to understand API creation, request validation, and response models.

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn

## Concepts Used

### FastAPI
Used to create the API and define endpoints like `GET` and `POST`.

```python
app = FastAPI()
```

### BaseModel
`BaseModel` is provided by Pydantic and is used to create data models.

```python
class CreateEmployee(BaseModel):
```

It helps FastAPI validate incoming data.

### CreateEmployee
A Pydantic model used for **request/input data** when creating an employee.

```python
class CreateEmployee(BaseModel):
    id: int
    name: str
    username: str
    email: str
    password: str
```

### EmployeeResponse
A Pydantic model used to define **what data should be returned** to the client.

```python
class EmployeeResponse(BaseModel):
    id: int
    name: str
    username: str
    email: str
```

The password is not included in the response.

### Field
`Field()` is used to add validation rules.

```python
id: int = Field(gt=0)
name: str = Field(min_length=3)
password: str = Field(min_length=8)
```

- `gt=0` → value must be greater than 0
- `min_length=3` → minimum 3 characters
- `min_length=8` → minimum 8 characters

### response_model
`response_model` defines the structure of the API response.

```python
@app.get("/employee", response_model=List[EmployeeResponse])
```

It also helps prevent unwanted fields such as passwords from being returned.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/employee` | Get all employees |
| POST | `/create/employee` | Create a new employee |

## Flow

```text
Request
   ↓
FastAPI
   ↓
Pydantic Validation
   ↓
CreateEmployee
   ↓
API Logic
   ↓
EmployeeResponse
   ↓
Response
```