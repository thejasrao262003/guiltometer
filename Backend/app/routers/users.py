from fastapi import APIRouter, Depends, Header
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.users import UserCreate, UserLogin, UpdateUser, Token
from app.utils.auth import get_current_user
from app.database import get_db
from app.services.users import *

router = APIRouter(tags=["User"])

@router.post("/signup", summary="Register a new user")
async def signup_route(
    user: UserCreate, 
    db: AsyncSession = Depends(get_db)
):
    return await create_user(db, user)

@router.post("/login", response_model=Token, summary="Authenticate and get access token")
async def login_route(
    user_login: UserLogin, 
    db: AsyncSession = Depends(get_db)
):
    return await login_user(db, user_login)

@router.post("/refresh-token", summary="Refresh JWT token")
async def refresh_token_route(
    authorization: str = Header(..., alias="Authorization")
):
    return await refresh_token(authorization)

@router.patch("/me", summary="Update current user")
async def update_user_route(
    update_user_data: UpdateUser,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await update_user_details(db, update_user_data, current_user["id"])

@router.get("/me", summary="Get current user details")
async def get_user_details_route(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user_id = current_user["id"]
    return await get_user_details(db=db, user_id=user_id)

@router.delete("/me", summary="Delete current user account")
async def delete_user_route(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user_id = current_user["id"]
    return await delete_user(db=db, user_id=user_id)
