from fastapi import APIRouter, HTTPException, Path
from schema.employee import CreateEmployee, EmployeeResponse, UpdateUser
from starlette import status
from dependencies import db_dependency
from typing import List
from models.employee import Employee

router = APIRouter(
    prefix='/employee',
    tags=['EMPLOYEE']
)

@router.get('/', response_model = List[EmployeeResponse], status_code = status.HTTP_200_OK)
async def get_all_employee(db: db_dependency):
    return db.query(Employee).all()

@router.get('/{id}', response_model = EmployeeResponse, status_code = status.HTTP_200_OK)
async def get_emp_by_id(db: db_dependency, id: int = Path(gt = 0)):
    emp = db.query(Employee).filter(Employee.id == id).first()
    if emp is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'employee not found')
    return emp

@router.post('/create_user', response_model = EmployeeResponse, status_code = status.HTTP_201_CREATED)
async def create_new_user(db: db_dependency, user: CreateEmployee):
    emp = db.query(Employee).filter(Employee.username == user.username).first()
    if emp is not None:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = 'user already exist')
    new_emp = Employee (
        username = user.username,
        name = user.name,
        email_id = user.email_id,
        passsword = user.password,
    )
    
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    
    return new_emp

@router.put('/update_user/{id}', response_model=EmployeeResponse)
async def update_user_by_id(db: db_dependency, user: UpdateUser, id: int = Path(gt = 0)):
    if db.query(Employee).filter(Employee.id != id).first():
        raise HTTPException(status_code = status.HTTP_404, detail = 'user not found')
    existing_user = db.query(Employee).filter(Employee.id == id).first()
    existing_user.name = user.name
    existing_user.username = user.username
    
    db.commit()
    db.refresh(existing_user)
    return existing_user


@router.delete('/delete_user/{id}')
async def delete_user_by_id(db: db_dependency, id: int = Path(gt = 0)):
    if db.query(Employee).filter(Employee.id != id).first():
        raise HTTPException(status_code = status.HTTP_404, detail = 'user not found')
    existing_user = db.query(Employee).filter(Employee.id == id).first()  
    db.delete(existing_user)
    db.commit()
    
    return {'msg': 'User is deleted'}
    
    
