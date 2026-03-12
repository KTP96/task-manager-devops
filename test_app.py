import json
import app as task_app_module

app = task_app_module.app

def setup_function():
    task_app_module.tasks.clear()
    task_app_module.next_id = 1

def test_get_tasks_initially_empty():
    client = app.test_client()
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert response.get_json() == []

def test_add_task():
    client = app.test_client()
    response = client.post(
        "/api/tasks",
        data=json.dumps({"title": "Learn DevOps"}),
        content_type="application/json"
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Learn DevOps"
    assert data["done"] is False

def test_add_task_invalid():
    client = app.test_client()
    response = client.post(
        "/api/tasks",
        data=json.dumps({"title": ""}),
        content_type="application/json"
    )
    assert response.status_code == 400

def test_toggle_task():
    client = app.test_client()
    create_response = client.post(
        "/api/tasks",
        data=json.dumps({"title": "Practice Docker"}),
        content_type="application/json"
    )

    task_id = create_response.get_json()["id"]
    response = client.put(f"/api/tasks/{task_id}")
    assert response.status_code == 200
    data = response.get_json()
    assert data["done"] is True

def test_delete_task():
    client = app.test_client()
    create_response = client.post(
        "/api/tasks",
        data=json.dumps({"title": "Practice CI/CD"}),
        content_type="application/json"
    )

    task_id = create_response.get_json()["id"]
    response = client.delete(f"/api/tasks/{task_id}")
    assert response.status_code == 200