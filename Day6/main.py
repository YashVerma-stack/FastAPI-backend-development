from fastapi import FastAPI
from database import Base, engine
from models import employee
from dependencies import db_dependency
from routers import employee

Base.metadata.create_all(bind = engine)
app =  FastAPI(title = 'Day 6 - Database Setup & Introduction')

app.include_router(employee.router)

@app.get('/')
async def home():
    return {
        'msg': 'Welcome Home'
    }
    