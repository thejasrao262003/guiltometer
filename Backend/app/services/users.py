from fastapi import HTTPException, Header
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from app.models.users import User
from app.schemas.users import UserCreate, UserLogin, UpdateUser
import uuid
from app.utils.auth import (
    hash_password, verify_password,
    create_access_token, create_refresh_token,
    decode_access_token
)
from datetime import datetime, UTC
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY_ENV")
ALGORITHM = os.getenv("ALGORITHM_ENV", "HS256")


async def create_user(db: AsyncSession, user_data: UserCreate) -> User:
    encrypted_password = hash_password(user_data.password)
    new_user = User(
        id=uuid.uuid4(),
        email=user_data.email,
        user_name=user_data.user_name,
        api_key=user_data.api_key,
        encrypted_password=encrypted_password,
        created_at=datetime.now(UTC)
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


async def login_user(db: AsyncSession, login_data: UserLogin):
    query = select(User).where(User.email == login_data.email)
    result = await db.execute(query)
    user = result.scalars().first()

    if not user or not verify_password(login_data.password, user.encrypted_password):
        raise HTTPException(status_code=401, detail="Invalid Credentials")

    user_id = str(user.id)
    access_token = create_access_token({"sub": user_id})
    refresh_token = create_refresh_token({"sub": user_id})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "message": "Login successful"
    }


async def refresh_token(authorization: str = Header(...)):
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=401, detail="Invalid auth scheme")

        payload = decode_access_token(token)
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token payload")

        new_token = create_access_token({"sub": user_id})
        return {"access_token": new_token, "token_type": "bearer"}

    except Exception:
        raise HTTPException(status_code=401, detail="Invalid refresh token")


async def update_user_details(db: AsyncSession, update_data: UpdateUser, user_id: uuid.UUID) -> dict:
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    for field, value in update_data.dict(exclude_unset=True).items():
        setattr(user, field, value)

    await db.commit()
    await db.refresh(user)

    return {
        "message": "User updated successfully",
        "user": {
            "id": user.id,
            "email": user.email,
            "api_key": user.api_key,
            "user_name": user.user_name
        }
    }

async def delete_user(db: AsyncSession, user_id: uuid.UUID)->dict:
    query = select(User).where(User.id==user_id)
    result = await db.execute(query)
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    await db.delete(user)
    await db.commit()

    return {"message": "User deleted successfully"}

async def get_user_details(db: AsyncSession, user_id: uuid.UUID)->dict:
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "id": user.id,
        "email": user.email,
        "user_name": user.user_name,
        "api_key": user.api_key,
        "created_at": user.created_at,
    }