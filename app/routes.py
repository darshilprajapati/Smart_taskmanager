from flask import (
    Blueprint,
    render_template,
    request,
    jsonify
)
from app.analytics import generate_task_analytics
from flask_login import (
    login_required,
    current_user
)

from app import db
from app.models import Task


routes = Blueprint(
    "routes",
    __name__
)


@routes.route("/")
@login_required
def home():

    tasks = Task.query.filter_by(
        user_id=current_user.id
    ).all()

    analytics = generate_task_analytics(
        current_user.id
    )

    return render_template(
        "index.html",
        tasks=tasks,
        analytics=analytics
    )

@routes.route("/api/tasks", methods=["GET"])
@login_required
def get_tasks():

    tasks = Task.query.filter_by(
        user_id=current_user.id
    ).all()

    task_list = []

    for task in tasks:

        task_list.append({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "priority": task.priority,
            "status": task.status
        })

    return jsonify(task_list)


@routes.route("/api/tasks", methods=["POST"])
@login_required
def add_task():

    data = request.json

    new_task = Task(
        title=data["title"],
        description=data["description"],
        priority=data["priority"],
        status=data["status"],
        user_id=current_user.id
    )

    db.session.add(new_task)

    db.session.commit()

    return jsonify({
        "message": "Task added successfully"
    })


@routes.route("/api/tasks/<int:task_id>", methods=["PUT"])
@login_required
def update_task(task_id):

    task = Task.query.get_or_404(task_id)

    data = request.json

    task.title = data.get(
        "title",
        task.title
    )

    task.description = data.get(
        "description",
        task.description
    )

    task.priority = data.get(
        "priority",
        task.priority
    )

    task.status = data.get(
        "status",
        task.status
    )

    db.session.commit()

    return jsonify({
        "message": "Task updated successfully"
    })


@routes.route("/api/tasks/<int:task_id>", methods=["DELETE"])
@login_required
def delete_task(task_id):

    task = Task.query.get_or_404(task_id)

    db.session.delete(task)

    db.session.commit()

    return jsonify({
        "message": "Task deleted successfully"
    })