from flask import Blueprint, request, jsonify
from models.task import Task
from utils.helper import auto_priority
from app import db

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data.get("title") or not data.get("deadline"):
        return jsonify({"error": "Missing fields"}), 400

    priority = auto_priority(data["deadline"])

    task = Task(
        title=data["title"],
        deadline=data["deadline"],
        priority=priority,
        status="pending"
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({"message": "Task created", "task": task.to_dict()})


@task_bp.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])


@task_bp.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = Task.query.get(id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    task.status = "completed"
    db.session.commit()

    return jsonify({"message": "Task updated"})


@task_bp.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = Task.query.get(id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Task deleted"})
