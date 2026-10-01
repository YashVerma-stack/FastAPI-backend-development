from fastapi import FastAPI
from models import employee
from database import Base, engine

Base.metadata.create_all(bind = engine)

app = FastAPI(title='Day 5 - Setting the Database')


@app.get('/home')
async def home():
    return {'mag': 'welcome to the fastapi'}