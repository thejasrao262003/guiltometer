from fastapi import APIRouter, Depends
from app.schemas.tasks import TaskCreate, TaskUpdate
from app.models.users import User
from app.utils.auth import get_current_user
from app.database import get_db
from app.services.tasks import *

router = APIRouter(tags=["Task"])

@router.post("")
async def create_task_route( 
    task_create: TaskCreate,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    user_id = user["id"]
    return await create_task(db, task_create, user_id=user_id)

@router.patch("/{task_id}")
async def update_task_route(
    task_id: uuid.UUID,
    task_update: TaskUpdate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user)
):
    user_id = user["id"]
    return await update_task(db=db, task_id=task_id, task_update=task_update, user_id=user_id)

@router.delete("/{task_id}")
async def delete_task_route(
    task_id: uuid.UUID,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    user_id = user["id"]
    return await delete_task(db=db, task_id=task_id, user_id=user_id)

@router.get("")
async def get_all_tasks_route(
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    user_id = user["id"]
    return await get_tasks_details(db=db, user_id=user_id)

@router.get("/{task_id}")
async def get_task_detail_route(
    task_id: uuid.UUID,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    user_id = user["id"]
    return await get_task_detail(db=db, task_id=task_id, user_id=user_id)