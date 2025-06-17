from app.schemas.tasks import TaskCreate, TaskUpdate
from app.models.tasks import Task
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
import uuid
from fastapi import HTTPException
from datetime import datetime, UTC

async def create_task(db: AsyncSession, task_create: TaskCreate, user_id: uuid.UUID) -> Task:
    new_task = Task(
        id = uuid.uuid4,
        user_id = user_id,
        name = task_create.name,
        category = task_create.category,
        target_frequency = task_create.target_frequency,
        expected_duration_days = task_create.expected_duration_days,
        roadmap_enabled = task_create.roadmap_enabled,
        created_at =datetime.now(UTC),
        description = task_create.description
    )

    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task

async def update_task(db:AsyncSession, task_id: uuid.UUID, user_id: uuid.UUID, task_update: TaskUpdate):
    result = await db.execute(
        select(Task).where(Task.id == task_id, Task.user_id == user_id)
    )
    task = result.scalar.first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    update_data = task_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)

    await db.commit()
    await db.refresh(task)

    return {
        "id": str(task.id),
        "message": "Task updated successfully",
        "updated_fields": update_data
    }

async def delete_task(db:AsyncSession, task_id: uuid.UUID, user_id: uuid.UUID):
    query = select(Task).where(Task.id==task_id, Task.user_id == user_id)
    result = await db.execute(query)
    task = result.scalars().first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    await db.delete(task)
    await db.commit()

    return {"message": "Task deleted succesfully"}

async def get_tasks_details(db: AsyncSession, user_id: uuid.UUID) -> list[Task]:
    query = select(Task).where(Task.user_id == user_id)
    results = await db.execute(query)
    tasks = results.scalars().all()

    return [
        {
            "id": str(task.id),
            "name": task.name,
            "category": task.category,
            "start_date": task.start_date.isoformat() if task.start_date else None,
            "target_frequency": task.target_frequency,
            "expected_duration_days": task.expected_duration_days,
            "roadmap_enabled": task.roadmap_enabled,
            "description": task.description,
            "created_at": task.created_at.isoformat() if task.created_at else None
        }
        for task in tasks

    ]

async def get_task_detail(db: AsyncSession, task_id: uuid.uuid4, user_id: uuid.uuid4) -> Task:
    query = select(Task).where(Task.id == task_id, Task.user_id == user_id)
    result = await db.execute(query)
    task = result.scalars().first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return task

