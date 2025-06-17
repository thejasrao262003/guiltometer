from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from app.schemas.roadmaps import RoadmapCreate, RoadmapUpdate, RoadmapOut
from app.services.roadmaps import (
    create_roadmap,
    update_roadmap,
    delete_roadmap,
    get_roadmaps_by_task,
    get_roadmap_detail,
)
from app.database import get_db
from app.utils.auth import get_current_user
from app.models.users import User

router = APIRouter(tags=["Roadmap"])

@router.post("/roadmaps", response_model=RoadmapOut)
async def create_roadmap_route(
    roadmap_create: RoadmapCreate,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await create_roadmap(db, roadmap_create)

@router.patch("/roadmaps/{roadmap_id}")
async def update_roadmap_route(
    roadmap_id: UUID,
    roadmap_update: RoadmapUpdate,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await update_roadmap(db, roadmap_id, roadmap_update)

@router.delete("/roadmaps/{roadmap_id}")
async def delete_roadmap_route(
    roadmap_id: UUID,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await delete_roadmap(db, roadmap_id)

@router.get("/roadmaps/task/{task_id}", response_model=list[RoadmapOut])
async def get_roadmaps_by_task_route(
    task_id: UUID,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await get_roadmaps_by_task(db, task_id)

@router.get("/roadmaps/{roadmap_id}", response_model=RoadmapOut)
async def get_roadmap_detail_route(
    roadmap_id: UUID,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    return await get_roadmap_detail(db, roadmap_id)
