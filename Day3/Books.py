from fastapi import FastAPI, Body

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

@app.get('/books/{title}')
async def get_book_by_title(title: str):
    book_to_return = []
    for book in BOOKS:
        if book.get('title').casefold() == title.casefold():
            book_to_return.append(book)
    return book_to_return

@app.get('/books/author/{author}')
async def get_book_by_author(author: str):
    book_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            book_to_return.append(book)
    return book_to_return

@app.post('/books/create-book')
async def create_book(new_book = Body()):
    BOOKS.append(new_book)
    
@app.put('/books/updated-books')
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book 

@app.delete('/books/delete_book/{book_title}')
async def delete_book(book_title : str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
    
