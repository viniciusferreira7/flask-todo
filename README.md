# Flask ToDo API

> 🚀 Study project - Complete task management API with full CRUD operations

A fully-featured task management API built with Flask. This is a comprehensive learning project from Rocketseat's Backend with Python track that demonstrates core backend development concepts including REST API design, request validation, error handling, and comprehensive test coverage.

## Project Status

✅ **Complete Core Implementation** - All CRUD operations fully implemented and tested. Comprehensive test suite covers all endpoints.

## Features

- ✅ **Create Tasks** (POST /tasks) - Add new tasks with title and description
- ✅ **List All Tasks** (GET /tasks) - Retrieve all tasks with total count
- ✅ **Get Task by ID** (GET /tasks/<id>) - Fetch a specific task
- ✅ **Update Tasks** (PATCH /tasks/<id>) - Modify task details and completion status
- ✅ **Delete Tasks** (DELETE /tasks/<id>) - Remove tasks permanently
- ✅ **Automatic API Documentation** - Swagger/OpenAPI docs auto-generated at /apidocs/
- ✅ **Comprehensive Test Suite** - Full integration testing with pytest

## Technologies Used

- **Python 3.7+** - Modern Python runtime
- **Flask 2.3.0** - Lightweight web framework for building REST APIs
- **Werkzeug 2.3.0** - WSGI utilities and development server
- **Flasgger** - Swagger/OpenAPI documentation for Flask
- **Requests 2.31.0** - HTTP client library for testing
- **Pytest 7.4.3** - Modern Python testing framework for integration tests

## Project Structure

```
flask-todo/
├── app/
│   ├── models/
│   │   └── task.py              # Task model class with domain logic
│   ├── schemas/
│   │   └── task.py              # Task TypedDict schema for type hints
│   ├── routes/
│   │   └── task_route.py        # Route handlers with business logic
│   └── app.py                   # Main Flask application & route registration
├── tests.py                     # Comprehensive integration test suite
├── requirements.txt             # Project dependencies
└── README.md                    # This documentation file
```

### Directory Details

**`app/`** - Main application package
- **`models/task.py`** - Task model class managing task properties and conversion methods
- **`schemas/task.py`** - TypedDict schema defining task data structure and types
- **`routes/task_route.py`** - Business logic for all CRUD operations
- **`app.py`** - Flask app initialization, route registration, and Swagger configuration

**Root Files**
- **`tests.py`** - Integration tests covering all 5 endpoints with full CRUD operations
- **`requirements.txt`** - pip dependencies (Flask, Pytest, Requests, etc.)
- **`README.md`** - Project documentation

## How to Use

### Prerequisites

- **Python 3.7+** - Ensure you have Python installed on your system
- **pip** - Python package manager (comes with Python 3.7+)
- **Virtual environment** - Recommended for dependency isolation

### Installation Steps

1. Clone the repository:
```bash
git clone <your-repository>
cd flask-todo
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

This installs Flask, Flasgger, Requests, and Pytest as specified in requirements.txt.

### Running the Application

**Start the development server:**
```bash
python app/app.py
```

**Access the application:**
- **API Server:** http://localhost:5001
- **Interactive API Docs (Swagger):** http://localhost:5001/apidocs/
- **ReDoc Docs:** http://localhost:5001/redoc/

### Running Tests

**Execute the full test suite:**
```bash
pytest tests.py
```

Or with verbose output:
```bash
pytest tests.py -v
```

**Note:** The test server must be running (in another terminal) for tests to pass, as they perform integration tests against the live API.

## Available Endpoints

All endpoints return JSON responses and support standard HTTP status codes. Base URL: `http://localhost:5001`

### 1. Create Task
**POST** `/tasks`

Creates a new task with the provided title and description.

**Request Body:**
```json
{
  "title": "Study Flask",
  "description": "Learn how to build APIs with Flask"
}
```

**Response (201 Created)**
```json
{
  "message": "New task created successfully"
}
```

**Requirements:**
- `title` (string, required) - Task title
- `description` (string, required) - Task description

---

### 2. List All Tasks
**GET** `/tasks`

Retrieves all tasks with pagination information.

**Response (200 OK)**
```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Study Flask",
      "description": "Learn how to build APIs with Flask",
      "is_completed": false
    }
  ],
  "total_tasks": 1
}
```

**Returns:**
- `tasks` (array) - List of all tasks
- `total_tasks` (number) - Count of total tasks

---

### 3. Get Task by ID
**GET** `/tasks/<id>`

Retrieves a specific task by its ID.

**Path Parameters:**
- `id` (integer, required) - Task ID

**Response (200 OK)**
```json
{
  "task": {
    "id": 1,
    "title": "Study Flask",
    "description": "Learn how to build APIs with Flask",
    "is_completed": false
  }
}
```

**Response (404 Not Found)**
```json
{
  "message": "Task not found"
}
```

---

### 4. Update Task
**PATCH** `/tasks/<id>`

Updates a specific task's properties. All fields are optional.

**Path Parameters:**
- `id` (integer, required) - Task ID

**Request Body (all optional):**
```json
{
  "title": "Study Flask Advanced",
  "description": "Learn advanced Flask concepts and best practices",
  "is_completed": true
}
```

**Response (204 No Content)** - Successful update, no response body

**Response (404 Not Found)**
```json
{
  "message": "Task not found"
}
```

---

### 5. Delete Task
**DELETE** `/tasks/<id>`

Permanently removes a task from the database.

**Path Parameters:**
- `id` (integer, required) - Task ID

**Response (204 No Content)** - Task deleted successfully, no response body

**Response (404 Not Found)**
```json
{
  "message": "Not found"
}
```

---

## Response Status Codes

| Status | Meaning | Used By |
|--------|---------|---------|
| 200 | OK - Request successful | GET requests |
| 201 | Created - Resource created successfully | POST /tasks |
| 204 | No Content - Request successful, no content to return | PATCH, DELETE |
| 404 | Not Found - Resource doesn't exist | GET, PATCH, DELETE with invalid ID |

## Data Model

### Task Object
```typescript
{
  id: number          // Unique task identifier (auto-generated)
  title: string       // Task title (required)
  description: string // Task description (required)
  is_completed: boolean // Completion status (default: false)
}
```

## Architecture & Design

### Project Design Patterns

**Separation of Concerns:**
- **Models** (`app/models/`) - Domain objects and data structures
- **Schemas** (`app/schemas/`) - Type definitions using TypedDict for type safety
- **Routes** (`app/routes/`) - Business logic and request handling
- **Application** (`app/app.py`) - Flask app initialization and route registration

**Data Flow:**
```
HTTP Request → Flask Route Handler → Business Logic (routes) → Data Model → Response
```

### Type Safety
The project uses Python's `TypedDict` for type hints, providing static type checking without runtime overhead.

### Testing Architecture
- **Integration Tests** - Tests run against a live server instance
- **Test Coverage** - All 5 endpoints covered with success and error cases
- **Test Utilities** - Helper functions reduce code duplication

## Development Notes

## Testing

### Running Tests

Execute the full test suite:
```bash
pytest tests.py -v
```

### Test Coverage

The test suite includes integration tests for all endpoints:

| Endpoint | Test | Status |
|----------|------|--------|
| POST /tasks | `test_create_task()` | ✅ Implemented |
| GET /tasks | `test_get_tasks()` | ✅ Implemented |
| GET /tasks/<id> | `test_get_task()` | ✅ Implemented |
| PATCH /tasks/<id> | `test_update_task()` | ✅ Implemented |
| DELETE /tasks/<id> | `test_delete_task()` | ✅ Implemented |

### How to Run Tests with Server

1. **Terminal 1 - Start the server:**
```bash
python app/app.py
```

2. **Terminal 2 - Run tests:**
```bash
pytest tests.py -v
```

## Project Statistics

- **Files:** 7 core files (models, schemas, routes, app, tests)
- **Routes:** 5 endpoints (full CRUD operations)
- **Tests:** 5 integration test cases
- **Lines of Code:** ~200 (excluding tests)
- **Dependencies:** 4 core libraries

## Learning Outcomes

This project demonstrates:
- RESTful API design principles
- Flask framework fundamentals
- Request/response handling
- HTTP status codes and semantics
- JSON data serialization
- Type hints in Python
- Integration testing with Pytest
- Swagger/OpenAPI documentation
- Error handling and validation
- Code organization and separation of concerns

## Author

Developed during [Rocketseat](https://www.rocketseat.com.br) studies - Backend with Python track

## License

This project is open source and available for educational purposes.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve this learning project.