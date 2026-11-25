import pytest
from app import app, tasks

@pytest.fixture
def client():
    tasks.clear()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
    tasks.clear()

def test_homepage_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"DevOps Task Tracker" in response.data

def test_add_task(client):
    response = client.post("/", data={"task": "Complete DevOps Mini Project"})
    assert response.status_code == 302
    assert "Complete DevOps Mini Project" in tasks

def test_blank_task_is_not_added(client):
    response = client.post("/", data={"task": "   "})
    assert response.status_code == 302
    assert tasks == []

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {
        "service": "DevOps Task Tracker",
        "status": "healthy"
    }
