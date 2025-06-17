from app.models.weekly_reports import WeeklyReport
from app.schemas.weekly_reports import WeeklyReportCreate, WeeklyReportUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from uuid import UUID

async def create_weekly_report(db: AsyncSession, report_create: WeeklyReportCreate) -> WeeklyReport:
    new_report = WeeklyReport(**report_create.dict())
    db.add(new_report)
    await db.commit()
    await db.refresh(new_report)
    return new_report

async def update_weekly_report(db: AsyncSession, report_id: UUID, report_update: WeeklyReportUpdate):
    result = await db.execute(select(WeeklyReport).where(WeeklyReport.id == report_id))
    report = result.scalars().first()
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    
    for key, value in report_update.dict(exclude_unset=True).items():
        setattr(report, key, value)

    await db.commit()
    await db.refresh(report)
    return report

async def delete_weekly_report(db: AsyncSession, report_id: UUID):
    result = await db.execute(select(WeeklyReport).where(WeeklyReport.id == report_id))
    report = result.scalars().first()
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    
    await db.delete(report)
    await db.commit()
    return {"message": "Weekly report deleted successfully"}

async def get_weekly_reports_by_task(db: AsyncSession, task_id: UUID):
    result = await db.execute(select(WeeklyReport).where(WeeklyReport.task_id == task_id))
    return result.scalars().all()

async def get_weekly_report_detail(db: AsyncSession, report_id: UUID):
    result = await db.execute(select(WeeklyReport).where(WeeklyReport.id == report_id))
    report = result.scalars().first()
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    return report
