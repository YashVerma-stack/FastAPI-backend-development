from fastapi import FastAPI

app = FastAPI(title="FastAPI Request Method Logic")

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'maths'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'python'},
    {'title': 'Title Four', 'author': 'Author One', 'category': 'c++'},
    {'title': 'Title Five', 'author': 'Author One', 'category': 'javacript'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'java'},
    {'title': 'Title Seven', 'author': 'Author Three', 'category': 'dsa'},
    {'title': 'Title Eight', 'author': 'Author Two', 'category': 'spring boot'},
    {'title': 'Title Nine', 'author': 'Author Three', 'category': 'maths'},
    {'title': 'Title Ten', 'author': 'Author Two', 'category': 'FastAPI'}
]

@app.get('/books')
async def read_all_books():
    return BOOKS

