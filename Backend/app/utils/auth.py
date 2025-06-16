import bcrypt
import logging
from datetime import datetime, timedelta
from fastapi import HTTPException, Header
from jose import JWTError, jwt
import os
from dotenv import load_dotenv
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY_ENV")
ALGORITHM = os.getenv("ALGORITHM_ENV", "HS256")

def hash_password(password: str) -> str:
    logger.debug("Hashing password")
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    hashed_str = hashed.decode("utf-8")
    logger.debug(f"Generated hash: {hashed_str}")
    return hashed_str

def verify_password(plain_password: str, hashed_password: str) -> bool:
    logger.debug("Verifying password")
    try:
        result = bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))
        logger.debug(f"Password verification result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error during password verification: {e}")
        return False
    
def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=30))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    logger.debug(f"Created access token for: {data.get('sub')}")
    return encoded_jwt

def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=2)
    to_encode.update({"exp": expire})
    refresh_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    logger.debug(f"Created refresh token for: {data.get('sub')}")
    return refresh_jwt

def decode_access_token(token: str)->dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError as e:
        logger.error(f"JWT Decode Error: {e}")
        raise HTTPException(status_code=401, detail="Could not validate credentials - invalid token")

def get_current_user(authorization: str = Header(...)) -> dict:
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=401, detail="Invalid authentication scheme")

        logger.debug(f"Token: {token[:10]}...")  # Log only start of token
        payload = decode_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            logger.error("No 'sub' claim in token")
            raise HTTPException(status_code=401, detail="Invalid token payload")

        logger.debug(f"Authenticated user_id: {user_id}")
        return {"id": user_id}

    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid authorization header format")
    except Exception as e:
        logger.error(f"Authentication error: {e}")
        raise HTTPException(status_code=401, detail="Could not validate credentials")