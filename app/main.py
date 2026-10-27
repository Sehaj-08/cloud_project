from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import init_db
from app.routes.health import router as health_router
from app.routes.tasks import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize application resources during startup."""
    init_db()
    yield


app = FastAPI(
    title="Task Management API",
    description=(
        "A simple API built to learn application development, "
        "testing, containerization, and cloud deployment."
    ),
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(health_router)
app.include_router(tasks_router)