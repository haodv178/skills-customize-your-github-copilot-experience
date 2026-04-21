"""Starter code for Building REST APIs with FastAPI assignment.

Run with:
    uvicorn starter-code:app --reload
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookInput(BaseModel):
    title: str
    author: str
    year: int


# In-memory data store for the assignment.
books = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin", "year": 2008},
    {"id": 2, "title": "The Pragmatic Programmer", "author": "Andrew Hunt", "year": 1999},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Books API"}


@app.get("/books")
def get_books():
    return {"books": books}


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return {"book": book}
    raise HTTPException(status_code=404, detail="Book not found")


# Task 2: implement POST /books and PUT /books/{book_id}
# Suggested approach:
# 1) Create a new ID based on the max existing ID.
# 2) Append new books to the list.
# 3) Locate and update matching books by ID.
