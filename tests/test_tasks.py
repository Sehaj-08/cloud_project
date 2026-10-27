import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app import models
from app.database import Base, get_db
from app.main import app


@pytest.fixture
def client():
    # Create an isolated in-memory SQLite database for this test.
    test_engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    TestingSessionLocal = sessionmaker(
        bind=test_engine,
        autoflush=False,
        autocommit=False,
    )

    # Create the tables in the test database.
    Base.metadata.create_all(bind=test_engine)

    # Override the application's database dependency.
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    # Preserve any existing dependency overrides.
    original_overrides = app.dependency_overrides.copy()
    app.dependency_overrides[get_db] = override_get_db

    # Do not use the TestClient context manager here:
    # the tests initialize their own database and do not need
    # the application's normal startup database initialization.
    test_client = TestClient(app)

    try:
        yield test_client
    finally:
        # Restore the application configuration.
        app.dependency_overrides.clear()
        app.dependency_overrides.update(original_overrides)

        # Clean up the isolated test database.
        Base.metadata.drop_all(bind=test_engine)
        test_engine.dispose()


def test_list_tasks_returns_empty_list(client):
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == []


def test_create_task(client):
    payload = {
        "title": "Learn Docker",
        "description": "Understand images and containers",
    }

    response = client.post("/tasks", json=payload)

    assert response.status_code == 201

    task = response.json()

    assert task["id"] > 0
    assert task["title"] == "Learn Docker"
    assert task["description"] == "Understand images and containers"
    assert task["completed"] is False


def test_created_task_appears_in_task_list(client):
    payload = {
        "title": "Learn Terraform",
        "description": "Learn infrastructure as code",
    }

    create_response = client.post("/tasks", json=payload)

    assert create_response.status_code == 201

    task_id = create_response.json()["id"]

    list_response = client.get("/tasks")

    assert list_response.status_code == 200

    tasks = list_response.json()

    assert len(tasks) == 1
    assert tasks[0]["id"] == task_id
    assert tasks[0]["title"] == "Learn Terraform"


def test_create_task_rejects_empty_title(client):
    response = client.post(
        "/tasks",
        json={
            "title": "   ",
            "description": "This task has an invalid title",
        },
    )

    assert response.status_code == 422


def test_create_task_rejects_missing_title(client):
    response = client.post(
        "/tasks",
        json={
            "description": "A title is required",
        },
    )

    assert response.status_code == 422


def test_update_task_changes_only_provided_fields(client):
    create_response = client.post(
        "/tasks",
        json={
            "title": "Learn AWS",
            "description": "Study EC2 and IAM",
        },
    )

    assert create_response.status_code == 201

    task_id = create_response.json()["id"]

    update_response = client.patch(
        f"/tasks/{task_id}",
        json={"completed": True},
    )

    assert update_response.status_code == 200

    updated_task = update_response.json()

    assert updated_task["id"] == task_id
    assert updated_task["title"] == "Learn AWS"
    assert updated_task["description"] == "Study EC2 and IAM"
    assert updated_task["completed"] is True


def test_update_task_can_clear_description(client):
    create_response = client.post(
        "/tasks",
        json={
            "title": "Learn Linux",
            "description": "Initial description",
        },
    )

    assert create_response.status_code == 201

    task_id = create_response.json()["id"]

    update_response = client.patch(
        f"/tasks/{task_id}",
        json={"description": None},
    )

    assert update_response.status_code == 200
    assert update_response.json()["description"] is None


def test_update_nonexistent_task_returns_404(client):
    response = client.patch(
        "/tasks/999",
        json={"completed": True},
    )

    assert response.status_code == 404


def test_update_task_rejects_empty_body(client):
    response = client.patch("/tasks/1", json={})

    assert response.status_code == 422