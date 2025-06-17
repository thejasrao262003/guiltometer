from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from app.models.roadmaps import Roadmap
from app.schemas.roadmaps import RoadmapCreate, RoadmapUpdate
from uuid import UUID
from datetime import datetime, UTC

async def create_roadmap(db: AsyncSession, roadmap_create: RoadmapCreate) -> Roadmap:
    new_roadmap = Roadmap(
        task_id=roadmap_create.task_id,
        week_start_date=roadmap_create.week_start_date,
        roadmap_md=roadmap_create.roadmap_md,
        created_at=datetime.now(UTC)
    )
    db.add(new_roadmap)
    await db.commit()
    await db.refresh(new_roadmap)
    return new_roadmap

async def update_roadmap(db: AsyncSession, roadmap_id: UUID, roadmap_update: RoadmapUpdate):
    result = await db.execute(select(Roadmap).where(Roadmap.id == roadmap_id))
    roadmap = result.scalars().first()

    if not roadmap:
        raise HTTPException(status_code=404, detail="Roadmap not found")

    update_data = roadmap_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(roadmap, key, value)

    await db.commit()
    await db.refresh(roadmap)

    return {
        "id": str(roadmap.id),
        "message": "Roadmap updated successfully",
        "updated_fields": update_data
    }

async def delete_roadmap(db: AsyncSession, roadmap_id: UUID):
    result = await db.execute(select(Roadmap).where(Roadmap.id == roadmap_id))
    roadmap = result.scalars().first()

    if not roadmap:
        raise HTTPException(status_code=404, detail="Roadmap not found")

    await db.delete(roadmap)
    await db.commit()
    return {"message": "Roadmap deleted successfully"}

async def get_roadmaps_by_task(db: AsyncSession, task_id: UUID):
    result = await db.execute(select(Roadmap).where(Roadmap.task_id == task_id))
    return result.scalars().all()

async def get_roadmap_detail(db: AsyncSession, roadmap_id: UUID):
    result = await db.execute(select(Roadmap).where(Roadmap.id == roadmap_id))
    roadmap = result.scalars().first()

    if not roadmap:
        raise HTTPException(status_code=404, detail="Roadmap not found")

    return roadmap
