
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

Phase 0: Project scope and API contract.

Application implementation, cloud infrastructure, CI/CD, monitoring, and recovery will be completed in subsequent phases.
