# Simple User Management API

A FastAPI-based REST API for user management with SQLAlchemy ORM and SQLite database.

## Features

- **User CRUD Operations**: Create, read, update, and delete users
- **RESTful API**: Follows REST conventions with proper HTTP status codes
- **Database Integration**: SQLAlchemy ORM with SQLite database
- **Input Validation**: Pydantic models for request/response validation
- **Pagination**: Built-in pagination for listing users
- **Error Handling**: Proper HTTP error responses for edge cases

## Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **SQLite**: Lightweight database
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: ASGI server for running the application

## Project Structure

```
simple-app/
├── app/
│   ├── __init__.py
│   ├── app.py              # FastAPI application entry point
│   ├── database.py         # Database configuration
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py         # User model definition
│   └── api/
│       ├── __init__.py
│       └── users/
│           ├── __init__.py
│           ├── router.py    # User endpoints
│           ├── schemas.py   # Pydantic models
│           └── services.py  # Business logic
├── app.db                  # SQLite database file
├── requirements.txt        # Python dependencies
└── test.http              # HTTP test requests
```

## Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd simple-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   uvicorn app.app:app --reload
   ```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- **Interactive API docs**: http://localhost:8000/docs
- **Alternative API docs**: http://localhost:8000/redoc

## API Endpoints

### Base Endpoint
- `GET /` - Welcome message

### User Management

#### Create User
```http
POST /users/
Content-Type: application/json

{
    "email": "user@example.com",
    "username": "username",
    "full_name": "Full Name",
    "is_active": true
}
```

#### Get All Users
```http
GET /users/?skip=0&limit=100
```

#### Get User by ID
```http
GET /users/{user_id}
```

#### Update User
```http
PUT /users/{user_id}
Content-Type: application/json

{
    "email": "updated@example.com",
    "username": "updated_username",
    "full_name": "Updated Name",
    "is_active": true
}
```

#### Delete User
```http
DELETE /users/{user_id}
```

## User Model

The User model includes the following fields:

- `id` (Integer, Primary Key): Unique identifier
- `email` (String, Required): Unique email address
- `username` (String, Required): Unique username
- `full_name` (String, Optional): User's full name
- `is_active` (Boolean, Default: true): User account status
- `created_at` (DateTime): Account creation timestamp
- `updated_at` (DateTime): Last update timestamp

## Testing

Use the provided `test.http` file to test the API endpoints. This file contains pre-configured HTTP requests for all available endpoints.

### Example Test Requests

1. **Create a new user**:
   ```http
   POST http://localhost:8000/users/
   Content-Type: application/json

   {
       "email": "john.doe@example.com",
       "username": "johndoe",
       "full_name": "John Doe",
       "is_active": true
   }
   ```

2. **Get all users**:
   ```http
   GET http://localhost:8000/users/
   ```

3. **Get user by ID**:
   ```http
   GET http://localhost:8000/users/1
   ```

## Development

### Database

The application uses SQLite with SQLAlchemy ORM. The database file (`app.db`) is automatically created when the application starts.

### Adding New Features

1. **Models**: Add new models in `app/models/`
2. **Schemas**: Define Pydantic schemas in `app/api/{resource}/schemas.py`
3. **Services**: Implement business logic in `app/api/{resource}/services.py`
4. **Routes**: Create endpoints in `app/api/{resource}/router.py`

## Error Handling

The API includes proper error handling for:
- 404 Not Found: When requesting non-existent resources
- 422 Unprocessable Entity: Invalid request data
- 500 Internal Server Error: Server-side errors

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

For questions or issues, please open an issue in the repository. 