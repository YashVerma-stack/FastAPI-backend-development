from pydantic import BaseModel, Field

class CreateEmployee(BaseModel):
    
    name: str = Field(min_length=3)
    username: str = Field(min_length = 3)
    email_id: str
    password: str
    
class EmployeeResponse(BaseModel):
    
    id: int
    name: str
    username: str
    email_id: str
    
class UpdateUser(BaseModel):
    name: str
    username: str

    

    