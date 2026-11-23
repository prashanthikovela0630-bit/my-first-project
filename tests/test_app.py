import pytest
from app import app, tasks

@pytest.fixture
def client():
    app.config["TESTING"] = True
    tasks.clear()
    with app.test_client() as client:
        yield client
    tasks.clear()

def test_homepage_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"DevOps Task Tracker" in response.data

def test_add_task(client):
    response = client.post("/", data={"title": "Build Docker image"})
    assert response.status_code == 302
    assert "Build Docker image" in tasks

def test_blank_task_is_not_added(client):
    response = client.post("/", data={"title": "   "})
    assert response.status_code == 302
    assert len(tasks) == 0

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {
        "status": "healthy",
        "service": "DevOps Task Tracker"
    }
