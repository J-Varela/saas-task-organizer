from app import create_app, db
from flask import Flask

app = create_app()

# Optional: Temporary route to initialize the database on Render
# @app.route('/initdb')
# def initdb():
#     db.create_all()
#     return "Database initialized!"

if __name__ == '__main__':
    app.run(debug=True)

