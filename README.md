
# Secure Cloud Delivery Platform

A DevOps training and portfolio project that automates the testing, packaging, deployment, monitoring, and recovery of a small cloud application.

## Why this project exists

Deploying software is more than making an application available online. Engineers must also test changes, manage infrastructure, control access, monitor failures, and recover safely.

This project demonstrates those responsibilities using a small Task Management API.

## Architecture

Developer
  -> GitHub
  -> GitHub Actions
  -> Automated tests and security checks
  -> Docker image
  -> Amazon ECR
  -> AWS EC2 deployment
  -> Health verification and monitoring

Terraform manages the cloud infrastructure. IAM and GitHub OIDC control deployment access. AWS Systems Manager executes deployment commands on the server. Nginx handles incoming web traffic, and CloudWatch collects operational logs and metrics.

## Technology stack

- Python and FastAPI
- SQLite
- Docker
- GitHub Actions
- Trivy
- Terraform
- AWS EC2, ECR, IAM, Systems Manager and CloudWatch
- Nginx

## API endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /health | Check application health |
| GET | /version | Show the running version |
| GET | /tasks | List tasks |
| POST | /tasks | Create a task |
| PATCH | /tasks/{task_id} | Update a task |

## Local development

The application implementation will be added in Phase 1.

Planned setup commands:

1. Create a Python virtual environment.
2. Install dependencies from requirements.txt.
3. Start the application using Uvicorn.
4. Run automated tests.
5. Open the interactive API documentation at /docs.

Exact startup commands will be verified when the application is implemented.

## Project documentation

See docs/project-scope.md for the project objectives, API contract, technology choices, scope, and completion criteria.

## Security and cost

- Never commit credentials, passwords, or private keys.
- Use least-privilege AWS permissions.
- Configure an AWS budget alert before creating billable resources.
- Do not store real or sensitive user data in this demonstration.
- Verify and remove unused cloud resources.

## Current status

Phase 1: Local Application Development and Testing

Application Architecture

The Task Management API is built using Python and FastAPI. SQLAlchemy handles database operations, Pydantic validates incoming requests and defines response structures, and SQLite stores task data persistently.

The application is organized into the following components:

app/main.py — Initializes the FastAPI application and registers routes.

app/database.py — Configures the database connection and session management.

app/models.py — Defines the database model for tasks.

app/schemas.py — Defines request validation and response schemas.

app/crud.py — Implements task creation, retrieval, and update operations.

app/routes/health.py — Implements health and version endpoints.

app/routes/tasks.py — Implements task management endpoints.

tests/ — Contains automated tests for API behavior and validation.

Database and Persistence

The default database URL is:

sqlite:///./data/tasks.db

The database file is created under the data directory relative to the application's working directory, unless the DATABASE_URL environment variable specifies another location.

The application initializes the required database tables during startup.

To verify persistence:

Create a task through /docs.

Stop the application.

Start the application again.

Call GET /tasks.

Verify that the previously created task still exists.

The SQLite database file is local application data and must not be committed to Git.

Automated Testing

Run the test suite from the repository root:

python -m pytest -v

The tests cover:

Health endpoint behavior.

Application version handling.

Task creation and retrieval.

Invalid and missing input.

Partial task updates.

Updates for nonexistent tasks.

Database isolation during task tests.

The task tests use a separate in-memory SQLite database to avoid modifying the normal local database.

Phase 1 Completion Criteria

Phase 1 is complete when:

The application starts using the documented commands.

All required endpoints behave as expected.

Invalid requests return appropriate HTTP errors.

Automated tests pass.

Task data survives application restarts.

No passwords, tokens, database files, or other sensitive data are committed to Git.

Another person can follow the README to set up and verify the application locally.

