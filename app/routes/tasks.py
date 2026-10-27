from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


@router.get(
    "",
    response_model=list[schemas.TaskResponse],
)
def list_tasks(
    db: Session = Depends(get_db),
):
    """Return all stored tasks."""
    return crud.get_tasks(db)


@router.post(
    "",
    response_model=schemas.TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    task_data: schemas.TaskCreate,
    db: Session = Depends(get_db),
):
    """Create a task and return the saved record."""
    return crud.create_task(db, task_data)


@router.patch(
    "/{task_id}",
    response_model=schemas.TaskResponse,
)
def update_task(
    task_id: int,
    task_data: schemas.TaskUpdate,
    db: Session = Depends(get_db),
):
    """Update an existing task or return 404 if it does not exist."""
    task = crud.update_task(
        db=db,
        task_id=task_id,
        task_data=task_data,
    )

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} was not found",
        )

    return task