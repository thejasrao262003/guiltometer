from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.daily_logs import DailyLogCreate, DailyLogUpdate, DailyLogOut
from app.models.users import User
from app.utils.auth import get_current_user
from app.database import get_db
from app.services.daily_logs import *
import uuid

router = APIRouter(tags=["Daily Logs"])

@router.post("/{task_id}", response_model=DailyLogOut)
async def create_daily_log_route(
    task_id: uuid.UUID,
    log_create: DailyLogCreate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return await create_daily_log(db=db, log_create=log_create, task_id=task_id)


@router.patch("/{log_id}", response_model=dict)
async def update_daily_log_route(
    log_id: uuid.UUID,
    task_id: uuid.UUID,
    log_update: DailyLogUpdate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return await update_daily_log(db=db, log_id=log_id, task_id=task_id, log_update=log_update)


@router.delete("/{log_id}", response_model=dict)
async def delete_daily_log_route(
    log_id: uuid.UUID,
    task_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return await delete_daily_log(db=db, log_id=log_id, task_id=task_id)


@router.get("/task/{task_id}", response_model=list[DailyLogOut])
async def get_all_daily_logs_route(
    task_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return await get_all_daily_logs(db=db, task_id=task_id)


@router.get("/{log_id}", response_model=DailyLogOut)
async def get_single_daily_log_route(
    log_id: uuid.UUID,
    task_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return await get_single_daily_log(db=db, log_id=log_id, task_id=task_id)
