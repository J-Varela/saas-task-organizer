# setup.py
from app import create_app
from app import db  # adjust this if your db is defined in app.py

app = create_app()

with app.app_context():
    db.create_all()
