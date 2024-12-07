# School Blog API

This is a simple FastAPI-based API for managing blogs and users. It uses MongoDB as the database and Pydantic for data validation.

## Installation

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Endpoints

### Blogs
- `GET /blogs`: Get all blogs.
- `POST /blogs`: Create a new blog.

### Users
- `GET /users`: Get all users.
- `POST /users`: Create a new user.

## Database

Ensure MongoDB is running locally or update the `MONGO_DETAILS` in `app/services/database.py` to connect to your MongoDB instance.
