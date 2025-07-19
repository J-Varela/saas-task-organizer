# SaaS Task Organizer

A simple SaaS-style web application for organizing tasks. Built with Flask, Flask-Login, and Flask-SQLAlchemy.

## Features

- User authentication (signup, login, logout)
- Add, complete, and delete tasks
- Tasks are user-specific
- SQLite database for persistence
- Bootstrap for UI styling

## Getting Started

### Prerequisites

- Python 3.10+
- See [requirements.txt](requirements.txt) for dependencies

### Installation

1. Clone the repository:
2. Install dependencies:
3. Run the application:
4. Access the app at [http://localhost:5000](http://localhost:5000)

### Project Structure

- `app/` - Main application package
  - `models.py` - Database models ([app/models.py](app/models.py))
  - `routes/` - Blueprints for authentication and tasks ([app/routes/auth.py](app/routes/auth.py), [app/routes/tasks.py](app/routes/tasks.py))
  - `templates/` - HTML templates ([app/templates/base.html](app/templates/base.html), etc.)
  - `static/` - Static files (CSS)
- `config.py` - Configuration ([config.py](config.py))
- `run.py` - Entry point ([run.py](run.py))
- `requirements.txt` - Python dependencies ([requirements.txt](requirements.txt))
- `instance/db.sqlite3` - SQLite database

## License

MIT
