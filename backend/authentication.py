
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from database.user import find_user
from passlib.context import CryptContext
from typing import Optional
from datetime import timedelta, datetime
from jose import JWTError, jwt
from utilities.config import config

security = HTTPBearer()

# Utility functions
def verify_password(plain_password, hashed_password):
    # Password hashing context
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    # Password hashing context
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    return pwd_context.hash(password)


async def authenticate_user(username: str, password: str):
    user = find_user(username)
    if not user:
        return False
    if not verify_password(password, user.user_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode,config.JWT_SECRET_KEY, algorithm=config.ALGORITHM)
    return encoded_jwt

async def get_user(token: str):
    payload = jwt.decode(token, config.JWT_SECRET_KEY, algorithms=[config.ALGORITHM])
    username: str = payload.get("sub")
    if username is None:
        raise JWTError
    user = find_user(username)
    if user is None:
        raise JWTError
    return user


def validate_jwt_bearer(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        payload = jwt.decode(token, config.JWT_SECRET_KEY, algorithms=[config.ALGORITHM])
        return payload  # Return decoded payload
    except:
        raise HTTPException(status_code=401, detail="Token has expired")
    # except jwt.ExpiredSignatureError:
    #     raise HTTPException(status_code=401, detail="Token has expired")
    # except jwt.InvalidTokenError:
    #     raise HTTPException(status_code=401, detail="Invalid token")
    
def validate_jwt_cookie(request: Request):
    try:
        token = request.cookies.get("MY_TOKEN")
        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unauthorized User"
            )
        payload = jwt.decode(token, config.JWT_SECRET_KEY, algorithms=[config.ALGORITHM])
        return payload  # Return decoded payload
    except:
        raise HTTPException(status_code=401, detail="Token has expired")
