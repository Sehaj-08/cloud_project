from fastapi.testclient import TestClient
from fastapi import status
from app.main import app


client = TestClient(app)


def test_health_returns_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

# Assuming this router is included in your main app instance
def test_health_check_v2(client: TestClient):
    response = client.get("/health2")
    assert response.status_code == status.HTTP_200_OK
    
    data = response.json()
    assert data["status"] == "active"
    assert data["deployment"] == "github-actions-ecr-live"