import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


# Use an environment variable when provided; otherwise use local SQLite.
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./data/tasks.db",
)

# Automatically create the directory for a file-based SQLite database.
if DATABASE_URL.startswith("sqlite:///"):
    database_path = DATABASE_URL.replace("sqlite:///", "", 1)

    if database_path != ":memory:":
        Path(database_path).expanduser().parent.mkdir(
            parents=True,
            exist_ok=True,
        )


# SQLite needs this option when connections may be used across threads.
connect_args = (
    {"check_same_thread": False}
    if DATABASE_URL.startswith("sqlite")
    else {}
)

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


# All SQLAlchemy models will inherit from this class.
class Base(DeclarativeBase):
    pass


def get_db():
    """Provide one database session for a request and close it afterward."""
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    """Create database tables defined by the application models."""
    # Import models so SQLAlchemy knows which tables exist.
    from app import models  # noqa: F401

    Base.metadata.create_all(bind=engine)