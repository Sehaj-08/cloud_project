import os

from fastapi import APIRouter


router = APIRouter(tags=["health"])


@router.get("/health")
def health_check() -> dict[str, str]:
    """Report that the application process is responding."""
    return {"status": "ok"}


@router.get("/version")
def get_version() -> dict[str, str]:
    """Return the version configured for this application release."""
    version = os.getenv("APP_VERSION", "0.1.0")

    return {"version": version}

@router.get("/health2")
def health_check_v2() -> dict[str, str]:
    """Dynamic check to verify that automated GitHub Actions deployments are live."""
    return {
        "status": "active",
        "deployment": "github-actions-ecr-live",
        "environment": os.getenv("APP_ENV", "production")
    }