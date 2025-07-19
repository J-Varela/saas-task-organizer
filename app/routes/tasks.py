from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .. import db
from ..models import Task

tasks = Blueprint('tasks', __name__)

@tasks.route('/')
def index():
    return redirect(url_for('auth.login'))

@tasks.route('/dashboard')
@login_required
def dashboard():
    user_tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('tasks.html', tasks=user_tasks)

@tasks.route('/add', methods=['POST'])
@login_required
def add_task():
    description = request.form.get('description')
    new_task = Task(description=description, user_id=current_user.id)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('tasks.dashboard'))

@tasks.route('/complete/<int:task_id>')
@login_required
def complete_task(task_id):
    task = Task.query.get(task_id)
    if task and task.user_id == current_user.id:
        task.is_complete = True
        db.session.commit()
    return redirect(url_for('tasks.dashboard'))

@tasks.route('/delete/<int:task_id>')
@login_required
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task and task.user_id == current_user.id:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('tasks.dashboard'))
