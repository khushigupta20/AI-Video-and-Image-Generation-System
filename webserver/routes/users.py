from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError

from backend.authentication import authenticate_user, create_access_token, get_user
from database.models import UserItem
from utilities.config import config

router = APIRouter()
# OAuth2 scheme for handling token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/user")
def register_user(user: UserItem):
    return user

# Endpoint to get a token
@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.user_email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# Dependency to get the current user
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        user = get_user(token)
    except JWTError:
        raise credentials_exception
    return user


# Protected route that requires a valid token
@router.get("/users/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user

# @app.post("/user")
# def register_user(user: UserItem):
#     return user

# # Endpoint to get a token
# @app.post("/token")
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(form_data.email, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user["username"]}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}


# # Dependency to get the current user
# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         user = get_user(token)
#     except JWTError:
#         raise credentials_exception
#     return user


# # Protected route that requires a valid token
# @app.get("/users/me")
# async def read_users_me(current_user: dict = Depends(get_current_user)):
#     return current_user