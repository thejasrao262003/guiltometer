from fastapi import APIRouter, Depends
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.weekly_reports import WeeklyReportCreate, WeeklyReportUpdate, WeeklyReportOut
from app.services.weekly_reports import (
    create_weekly_report,
    update_weekly_report,
    delete_weekly_report,
    get_weekly_reports_by_task,
    get_weekly_report_detail
)
from app.database import get_db
from app.utils.auth import get_current_user
from app.models.users import User

router = APIRouter(
    prefix="/weekly-reports",
    tags=["Weekly Reports"]
)

@router.post("", response_model=WeeklyReportOut)
async def create_weekly_report_route(
    report_create: WeeklyReportCreate,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await create_weekly_report(db, report_create)

@router.patch("/{report_id}", response_model=WeeklyReportOut)
async def update_weekly_report_route(
    report_id: UUID,
    report_update: WeeklyReportUpdate,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await update_weekly_report(db, report_id, report_update)

@router.delete("/{report_id}")
async def delete_weekly_report_route(
    report_id: UUID,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await delete_weekly_report(db, report_id)

@router.get("/task/{task_id}", response_model=list[WeeklyReportOut])
async def get_reports_by_task_route(
    task_id: UUID,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await get_weekly_reports_by_task(db, task_id)

@router.get("/{report_id}", response_model=WeeklyReportOut)
async def get_weekly_report_detail_route(
    report_id: UUID,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await get_weekly_report_detail(db, report_id)
