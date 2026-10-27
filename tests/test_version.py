from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_version_returns_default_version(monkeypatch):
    monkeypatch.delenv("APP_VERSION", raising=False)

    response = client.get("/version")

    assert response.status_code == 200
    assert response.json() == {"version": "0.1.0"}


def test_version_uses_environment_variable(monkeypatch):
    monkeypatch.setenv("APP_VERSION", "1.2.3")

    response = client.get("/version")

    assert response.status_code == 200
    assert response.json() == {"version": "1.2.3"}