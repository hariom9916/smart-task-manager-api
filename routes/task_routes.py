from flask import Blueprint, request, jsonify
from models.task import Task
from utils.helper import auto_priority

task_bp = Blueprint("tasks", __name__)

tasks = []

@task_bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data.get("title") or not data.get("deadline"):
        return jsonify({"error": "Missing fields"}), 400

    priority = auto_priority(data["deadline"])

    task = Task(data["title"], data["deadline"], priority)
    tasks.append(task)

    return jsonify({"message": "Task created", "task": task.to_dict()})


@task_bp.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify([task.to_dict() for task in tasks])


@task_bp.route("/tasks/<int:index>", methods=["PUT"])
def update_task(index):
    if index >= len(tasks):
        return jsonify({"error": "Task not found"}), 404

    tasks[index].status = "completed"
    return jsonify({"message": "Task updated"})


@task_bp.route("/tasks/<int:index>", methods=["DELETE"])
def delete_task(index):
    if index >= len(tasks):
        return jsonify({"error": "Task not found"}), 404

    tasks.pop(index)
    return jsonify({"message": "Task deleted"})
