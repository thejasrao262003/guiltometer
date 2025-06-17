from app.models.daily_logs import DailyLog
from app.schemas.daily_logs import DailyLogCreate, DailyLogUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from datetime import datetime
import uuid

async def create_daily_log(db: AsyncSession, log_create: DailyLogCreate, task_id: uuid.UUID) -> DailyLog:
    new_log = DailyLog(
        id=uuid.uuid4(),
        task_id=task_id,
        date=log_create.date,
        metrics=log_create.metrics,
        note=log_create.note,
        created_at=datetime.utcnow()
    )
    db.add(new_log)
    await db.commit()
    await db.refresh(new_log)
    return new_log


async def update_daily_log(
    db: AsyncSession, log_id: uuid.UUID, task_id: uuid.UUID, log_update: DailyLogUpdate
) -> dict:
    result = await db.execute(
        select(DailyLog).where(DailyLog.id == log_id, DailyLog.task_id == task_id)
    )
    log = result.scalars().first()

    if not log:
        raise HTTPException(status_code=404, detail="Daily log not found")

    update_data = log_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(log, key, value)

    await db.commit()
    await db.refresh(log)

    return {
        "id": str(log.id),
        "message": "Daily log updated successfully",
        "updated_fields": update_data
    }


async def delete_daily_log(db: AsyncSession, log_id: uuid.UUID, task_id: uuid.UUID) -> dict:
    result = await db.execute(
        select(DailyLog).where(DailyLog.id == log_id, DailyLog.task_id == task_id)
    )
    log = result.scalars().first()

    if not log:
        raise HTTPException(status_code=404, detail="Daily log not found")

    await db.delete(log)
    await db.commit()
    return {"message": "Daily log deleted successfully"}


async def get_all_daily_logs(db: AsyncSession, task_id: uuid.UUID) -> list[DailyLog]:
    result = await db.execute(select(DailyLog).where(DailyLog.task_id == task_id))
    return result.scalars().all()


async def get_single_daily_log(db: AsyncSession, log_id: uuid.UUID, task_id: uuid.UUID) -> DailyLog:
    result = await db.execute(
        select(DailyLog).where(DailyLog.id == log_id, DailyLog.task_id == task_id)
    )
    log = result.scalars().first()

    if not log:
        raise HTTPException(status_code=404, detail="Daily log not found")

    return log
