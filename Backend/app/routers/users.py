from fastapi import APIRouter, Depends
from app.schemas.users import UserCreate, UserLogin, UpdateUser, Token
from app.utils.auth import get_current_user
from app.database import get_db
from app.services.users import *
router = APIRouter(tags=["User"])

@router.post("/signup")
async def signup(
    user:UserCreate, 
    db: AsyncSession = Depends(get_db)
):
    return await create_user(db, user)

@router.post("/login", response_model=Token)
async def login(
    user_login: UserLogin, 
    db: AsyncSession = Depends(get_db)
):
    return await login_user(db, user_login)

@router.post("/refresh")
async def refresh_token_route(authorization: str = Header(..., alias="Authorization")):
    return await refresh_token(authorization)

@router.patch("/update_user")
async def update_user(
    update_user_data: UpdateUser,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await update_user_details(db, update_user_data, current_user["id"])

@router.get("/get_user_details")
async def get_user_details_router(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user_id = current_user["id"]
    return await get_user_details(db=db, user_id=user_id)

@router.delete("/delete_user")
async def delete_user_account(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user_id = current_user["id"]
    return await delete_user(db=db, user_id=user_id)