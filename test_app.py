from fastapi.testclient import TestClient
from main import app
#httpx added

client = TestClient(app)

def test_health():
    response = client.get("/")
    assert response.status_code == 200


def test_create_todo():
    res = client.post("/todos", json={
        "title": "test todo",
        "completed": False
    })
    assert res.status_code == 200
    data = res.json()
    assert "id" in data
    assert data["title"] == "test todo"
    return data["id"]

def test_get_todos():
    res = client.get("/todos")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_update_todo():
    create = client.post("/todos", json={
        "title": "update me",
        "completed": False
    }).json()

    res = client.put(f"/todos/{create['id']}", json={
        "title": "updated",
        "completed": True
    })
    assert res.status_code == 200
    assert res.json()["completed"] is True

def test_delete_todo():
    create = client.post("/todos", json={
        "title": "delete me",
        "completed": False
    }).json()

    res = client.delete(f"/todos/{create['id']}")
    assert res.status_code == 200