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