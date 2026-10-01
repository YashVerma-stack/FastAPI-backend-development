from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List


app = FastAPI()

EMPLOYEES = [
    {'id': 1, 'name': 'name1', 'username': 'emp1', 'email': 'emp1@gmail.com', 'password': '1234'},
    {'id': 2, 'name': 'name2', 'username': 'emp2', 'email': 'emp2@gmail.com', 'password': '1234'},
    {'id': 3, 'name': 'name3', 'username': 'emp3', 'email': 'emp3@gmail.com', 'password': '1234'},
    {'id': 4, 'name': 'name4', 'username': 'emp4', 'email': 'emp4@gmail.com', 'password': '1234'},
    {'id': 5, 'name': 'name5', 'username': 'emp5', 'email': 'emp5@gmail.com', 'password': '1234'},
    {'id': 6, 'name': 'name6', 'username': 'emp6', 'email': 'emp6@gmail.com', 'password': '1234'},
    {'id': 7, 'name': 'name7', 'username': 'emp7', 'email': 'emp7@gmail.com', 'password': '1234'},
    {'id': 8, 'name': 'name8', 'username': 'emp8', 'email': 'emp8@gmail.com', 'password': '1234'}
]

class CreateEmployee(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=3)
    username: str = Field(min_length=3)
    email: str
    password: str = Field(min_length=8)
    

    
class EmployeeResponse(BaseModel):
    id: int
    name: str
    username: str
    email: str

    # we create this to set the output that what we actually want to see in the response 
    
@app.get('/employee', response_model=List[EmployeeResponse])
async def get_all_emp():
    return EMPLOYEES
    
@app.post('/create/employee', response_model=EmployeeResponse)
async def create_emp(new_emp: CreateEmployee):
    create_new_emp = {}
    create_new_emp.update(new_emp)
    
    EMPLOYEES.append(create_new_emp)
    return create_new_emp
