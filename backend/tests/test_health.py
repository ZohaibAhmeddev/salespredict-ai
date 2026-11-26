
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health():
    response = client.get("/api/v1/health/")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_ping():
    response = client.get("/api/v1/health/ping")

    assert response.status_code == 200
    assert response.json()["message"] == "pong"


def test_sales():
    response = client.get("/api/v1/sales/")

    assert response.status_code == 200
    assert response.json()["total_records"] == 0
