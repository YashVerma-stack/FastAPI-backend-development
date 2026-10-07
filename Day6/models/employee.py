from database import Base
from sqlalchemy import Column, String, Boolean, Integer

class Employee(Base):
    __tablename__ = 'Employees'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, unique=True)
    email_id = Column(String, unique=True)
    hashedPasssword = Column(String)
    
