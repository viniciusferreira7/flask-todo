# Flask ToDo API

> 🚀 Study project under development (WIP)

A simple task management API built with Flask. This is a learning project to explore backend development concepts with Python and Flask.

## Project Status

⚠️ **Work In Progress (WIP)** - The project is under active development. Features may change or evolve.

## Features

- ✅ Create new tasks
- ✅ List all tasks
- 📋 Automatic documentation with Swagger

## Technologies Used

- **Python 3.x**
- **Flask** - Web framework
- **Flasgger** - Swagger/OpenAPI integration
- **Flask-SQLAlchemy** - ORM for database
- **Flask-CORS** - CORS support
- **Werkzeug** - Flask utilities

## Project Structure

```
flask-todo/
├── app/
│   ├── models/
│   │   └── task.py          # Task Model
│   ├── schemas/
│   │   └── task.py          # Task Schema
│   ├── routes/
│   │   └── task_route.py    # Task Routes
│   └── app.py               # Main Application
├── requirements.txt         # Project Dependencies
└── README.md               # This file
```

## How to Use

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation

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

### Running

To start the server:

```bash
python app/app.py
```

The server will be available at: `http://localhost:5001`

The interactive documentation (Swagger) will be at: `http://localhost:5001/apidocs/`

## Available Endpoints

### Create Task
**POST** `/tasks`

```json
{
  "title": "Study Flask",
  "description": "Learn how to build APIs with Flask"
}
```

**Response (201)**
```json
{
  "message": "New task created successfully"
}
```

### List Tasks
**GET** `/tasks`

**Response (200)**
```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Study Flask",
      "description": "Learn how to build APIs with Flask"
    }
  ],
  "total_tasks": 1
}
```

## Next Steps (Planned)

- [ ] Update tasks (PUT)
- [ ] Delete tasks (DELETE)
- [ ] Implement persistent database

## Development Notes

- The project uses an in-memory list to store tasks
- IDs are generated sequentially
- Data is lost when the application is restarted

## Author

Developed during Rocketseat studies - Backend with Python track

## License

This project is open source and available for educational purposes.