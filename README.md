# ms-reactor-api

## Overview
`ms-reactor-api` is a simple task management API built with FastAPI. It allows users to create, list, and delete tasks using an in-memory storage system. The application follows the principles of Clean Architecture, ensuring that the code is organized, maintainable, and easy to understand.

## Features
- Create a new task
- List all tasks
- Delete a task by ID

## Project Structure
```
ms-reactor-api
├── app
│   ├── api
│   │   ├── __init__.py
│   │   ├── dependencies.py
│   │   ├── task.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── config.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── task.py
│   ├── repositories
│   │   ├── __init__.py
│   │   ├── memory.py
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── task.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── task_service.py
│   ├── main.py
├── requirements.txt
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ms-reactor-api.git
   cd ms-reactor-api
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints
- **Create Task**: `POST /tasks`
- **List Tasks**: `GET /tasks`
- **Delete Task**: `DELETE /tasks/{task_id}`

## Contributing
Feel free to submit issues or pull requests to improve the project. 

## License
This project is licensed under the MIT License.