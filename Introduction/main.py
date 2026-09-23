from fastapi import FastAPI

app = FastAPI(title = "FastAPI-Tutorial")

@app.get('/home')
async def home():
    return "This is our first API"

# After code this we will have to enter the uvicorn main:app --relaod in the terminal 
# for the result we will go any of ther browser and visit http://127.0.0.1:8000/docs
# we will use the swagger ui for testing the APIs
