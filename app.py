from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tasks = []
next_id = 1


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@app.route("/api/tasks", methods=["POST"])
def add_task():
    global next_id

    data = request.get_json()
    title = data.get("title", "").strip()

    if not title:
        return jsonify({"error": "Task title is required"}), 400

    task = {
        "id": next_id,
        "title": title,
        "done": False
    }
    tasks.append(task)
    next_id += 1

    return jsonify(task), 201


@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
            return jsonify(task)

    return jsonify({"error": "Task not found"}), 404


@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    original_length = len(tasks)
    tasks = [task for task in tasks if task["id"] != task_id]

    if len(tasks) == original_length:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({"message": "Task deleted"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)