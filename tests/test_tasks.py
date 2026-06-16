from fastapi.testclient import TestClient
from schemas import TaskResponse
import pytest 

def test_create(client: TestClient):
    response = client.post("/tasks", json={"title": "test_post"})

    assert response.status_code == 200 
    assert response.json()["title"] == "test_post"
    assert response.json()["description"] == None
    assert response.json()["completed"] == False

def test_get_tasks(client: TestClient):
    response = client.get("/tasks")

    # before creation a task
    assert response.status_code == 200
    assert response.json() == []

    # after creating a task
    client.post("/tasks", json={"title": "test_get", "description": "all tasks"})
    response = client.get("/tasks")
    assert response.status_code == 200

    response = TaskResponse.model_validate(response.json()[0])

    assert isinstance(response, TaskResponse)
    assert response.title == "test_get"
    assert response.description == "all tasks"
    assert response.completed == False

def test_get_task(client: TestClient):
    # get 404
    assert client.get("/tasks/1").status_code == 404

    # getting an existing task
    client.post("/tasks", json={"title": "test_get_task"})
    response = client.get("/tasks/1")
    assert response.status_code == 200

    response = TaskResponse.model_validate(response.json())

    assert isinstance(response, TaskResponse)
    assert response.id == 1
    assert response.title == "test_get_task"
    assert response.completed == False

@pytest.mark.parametrize(
        argnames=["payload", "title", "description", "completed"],
        argvalues=[[{"title": "patch title"}, "patch title", None, False],
                   [{"title": "patch title and description", "description": "xz"}, "patch title and description", "xz", False],
                   [{"completed": True}, "poh", None, True]
                   ]
)
def test_patch(client: TestClient, payload, title, description, completed):
    client.post("/tasks", json={"title": "poh"})
    response = client.patch("/tasks/1", json=payload)
    assert response.status_code == 200

    response = TaskResponse.model_validate(response.json())

    assert isinstance(response, TaskResponse)
    assert response.title == title
    assert response.description == description
    assert response.completed == completed

def test_delete(client: TestClient):
    client.post("/tasks", json={"title": "test_delete"})

    assert client.delete("/tasks/1").status_code == 204
    assert client.delete("tasks/1").status_code == 404
