
# Secure Cloud Delivery Platform

## 1. Project purpose

Build a repeatable and secure process for testing, packaging, deploying, monitoring, and recovering a small application running in AWS.

The project focuses on learning practical DevOps engineering rather than building a complicated application.

## 2. Application

The application will be a Task Management API built with Python and FastAPI.

It will allow users to:
- Check whether the application is running.
- Identify the running application version.
- List tasks.
- Create tasks.
- Update existing tasks.

## 3. API contract

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /health | Check application health |
| GET | /version | Identify the running version |
| GET | /tasks | List tasks |
| POST | /tasks | Create a task |
| PATCH | /tasks/{task_id} | Update an existing task |

Invalid requests must return appropriate errors. Updating a task that does not exist must return HTTP 404.

## 4. Data storage

Use SQLite for task data.

Store the database in a persistent location outside the replaceable application container so that replacing the container does not erase task data.

The initial project uses one server and is not designed for multi-server database access.

## 5. Technology stack

- Python and FastAPI: application
- SQLite: data storage
- Git and GitHub: source control
- Docker: application packaging
- GitHub Actions: automated testing and deployment
- Trivy: security scanning
- Amazon ECR: container image registry
- AWS EC2: application server
- AWS IAM and GitHub OIDC: access control
- AWS Systems Manager: managed server access and deployment commands
- Nginx: web traffic routing
- Terraform: infrastructure as code
- Amazon CloudWatch: logs, metrics, and alarms

## 6. In scope

- Working Task Management API
- Automated application tests
- Docker image creation
- Automated security scanning
- AWS infrastructure managed with Terraform
- Automated deployment from GitHub
- Post-deployment health verification
- Logs and basic monitoring
- A tested deployment recovery procedure
- Documentation and cloud resource cleanup

## 7. Out of scope

- Kubernetes
- Multi-region deployment
- Automatic multi-server scaling
- Zero-downtime deployments
- A public platform for deploying arbitrary repositories
- A complicated frontend
- Production-grade multi-tenant user management

## 8. Success criteria

The project is complete when:

1. The application runs correctly.
2. Infrastructure can be created from Terraform configuration.
3. Automated tests can block an invalid release.
4. A successful application change reaches AWS through the deployment pipeline.
5. Application health is verified after deployment.
6. Logs help identify a deliberately introduced failure.
7. A failed release can be recovered using a tested procedure.
8. Setup, security decisions, limitations, and cleanup steps are documented.
