# Simple User Management API

A FastAPI-based REST API for user management with SQLAlchemy ORM, Alembic migrations, and SQLite database.

## Features

- **User CRUD Operations**: Create, read, update, and delete users
- **RESTful API**: Follows REST conventions with proper HTTP status codes
- **Database Integration**: SQLAlchemy ORM with SQLite database
- **Database Migrations**: Alembic for schema version control
- **Input Validation**: Pydantic models for request/response validation
- **Pagination**: Built-in pagination for listing users
- **Error Handling**: Proper HTTP error responses for edge cases

## Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **Alembic**: Database migration tool
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
├── alembic/                # Database migrations
│   ├── versions/           # Migration files
│   ├── env.py             # Alembic environment
│   └── script.py.mako     # Migration template
├── alembic.ini            # Alembic configuration
├── app.db                 # SQLite database file
├── requirements.txt       # Python dependencies
└── test.http             # HTTP test requests
```

## Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd simple-app
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**:
   ```bash
   alembic upgrade head
   ```

5. **Run the application**:
   ```bash
   uvicorn app.app:app --reload
   ```

The API will be available at `http://localhost:8000`

## Database Migrations

This project uses Alembic for database schema management. All database changes are version-controlled through migrations.

### Migration Commands

```bash
# View migration history
alembic history

# Check current migration state
alembic current

# Create a new migration (after model changes)
alembic revision --autogenerate -m "Description of changes"

# Apply pending migrations
alembic upgrade head

# Revert last migration
alembic downgrade -1

# Revert all migrations
alembic downgrade base
```

### Migration History

- **Initial Migration**: Created users table with basic fields
- **Latest Migration**: Added phone_number, date_of_birth, and role fields

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
    "phone_number": "+1234567890",
    "date_of_birth": "1990-01-01",
    "role": "user",
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
    "phone_number": "+1234567890",
    "date_of_birth": "1990-01-01",
    "role": "admin",
    "is_active": true
}
```

#### Delete User
```http
DELETE /users/{user_id}
```

## User Model

The User model includes the following fields:

### Core Fields
- `id` (Integer, Primary Key): Unique identifier
- `email` (String, Required, Unique): User's email address
- `username` (String, Required, Unique): User's username
- `full_name` (String, Optional): User's full name

### Profile Fields
- `phone_number` (String, Optional): User's phone number
- `date_of_birth` (Date, Optional): User's date of birth
- `role` (String, Required, Default: "user"): User's role in the system

### System Fields
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
       "phone_number": "+1234567890",
       "date_of_birth": "1990-01-01",
       "role": "user",
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

### Database Management

The application uses SQLite with SQLAlchemy ORM and Alembic for migrations.

#### Making Database Changes

1. **Modify the model** in `app/models/user.py`
2. **Generate migration**:
   ```bash
   alembic revision --autogenerate -m "Description of changes"
   ```
3. **Review the migration** file in `alembic/versions/`
4. **Apply the migration**:
   ```bash
   alembic upgrade head
   ```

#### Database Reset

To reset the database to a clean state:
```bash
# Remove database file
rm app.db

# Recreate database with migrations
alembic upgrade head
```

### Adding New Features

1. **Models**: Add new models in `app/models/`
2. **Migrations**: Generate migrations for model changes
3. **Schemas**: Define Pydantic schemas in `app/api/{resource}/schemas.py`
4. **Services**: Implement business logic in `app/api/{resource}/services.py`
5. **Routes**: Create endpoints in `app/api/{resource}/router.py`

### Code Quality

```bash
# Format code
black app/

# Run linting
flake8 app/

# Run type checking
mypy app/

# Run tests
pytest
```

## Error Handling

The API includes proper error handling for:
- 404 Not Found: When requesting non-existent resources
- 422 Unprocessable Entity: Invalid request data
- 500 Internal Server Error: Server-side errors

## Deployment

### Production Considerations

- Use PostgreSQL instead of SQLite for production
- Configure proper database connection pooling
- Set up environment variables for sensitive data
- Enable HTTPS
- Configure logging and monitoring

### Environment Variables

Create a `.env` file for configuration:
```env
DATABASE_URL=sqlite:///./app.db
SECRET_KEY=your-secret-key
DEBUG=False
```

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and ensure code quality
5. Create/update migrations if needed
6. Submit a pull request

### Commit Convention

This project follows [Conventional Commits](https://www.conventionalcommits.org/):

```bash
git commit -m "feat(models): add new user fields"
git commit -m "fix(api): resolve user creation issue"
git commit -m "docs(readme): update installation instructions"
```

## Support

For questions or issues, please open an issue in the repository.

## Changelog

### v1.1.0 (Current)
- Added phone_number, date_of_birth, and role fields to User model
- Implemented Alembic database migrations
- Enhanced project documentation

### v1.0.0
- Initial release with basic user CRUD operations
- FastAPI with SQLAlchemy integration
- RESTful API design 