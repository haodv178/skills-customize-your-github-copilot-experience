# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using FastAPI to practice creating endpoints, handling request data, and returning structured JSON responses.

## 📝 Tasks

### 🛠️ Create Core API Endpoints

#### Description
Set up a FastAPI application and create endpoints to manage a small in-memory collection of books.

#### Requirements
Completed program should:

- Create a FastAPI app in `starter-code.py`
- Add a `GET /` endpoint that returns a welcome message
- Add a `GET /books` endpoint that returns a list of all books
- Add a `GET /books/{book_id}` endpoint that returns one book by ID or an error if not found


### 🛠️ Add Create and Update Operations

#### Description
Expand your API so clients can add new books and update existing book records using JSON request bodies.

#### Requirements
Completed program should:

- Add a `POST /books` endpoint to create a new book with title, author, and year
- Add a `PUT /books/{book_id}` endpoint to update an existing book
- Validate request bodies using a Pydantic model
- Return clear JSON responses for success and failure cases
