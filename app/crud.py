from sqlalchemy.orm import Session

from app import models, schemas


def get_tasks(db: Session) -> list[models.Task]:
    """Return all tasks in ascending ID order."""
    return (
        db.query(models.Task)
        .order_by(models.Task.id.asc())
        .all()
    )


def create_task(
    db: Session,
    task_data: schemas.TaskCreate,
) -> models.Task:
    """Create and persist a new task."""
    db_task = models.Task(
        title=task_data.title,
        description=task_data.description,
        completed=False,
    )

    try:
        db.add(db_task)
        db.commit()
        db.refresh(db_task)

        return db_task

    except Exception:
        db.rollback()
        raise


def update_task(
    db: Session,
    task_id: int,
    task_data: schemas.TaskUpdate,
) -> models.Task | None:
    """
    Update an existing task.

    Return None if the task does not exist.
    Only fields explicitly provided in the request are changed.
    """
    db_task = db.get(models.Task, task_id)

    if db_task is None:
        return None

    update_data = task_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_task, field, value)

    try:
        db.commit()
        db.refresh(db_task)

        return db_task

    except Exception:
        db.rollback()
        raise