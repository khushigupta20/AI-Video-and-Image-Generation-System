from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from jose import JWTError

from backend.authentication import authenticate_user, create_access_token, get_user, validate_jwt_cookie
from database.models import UserItem
from utilities.config import config

router = APIRouter()
# OAuth2 scheme for handling token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

templates = Jinja2Templates(directory="static")

@router.get("/jobs/")
async def protected_test(request: Request, payload: dict = Depends(validate_jwt_cookie)):
    # return {"message": "This is a protected endpoint", "user_id": payload}
    return templates.TemplateResponse("jobs/index.html",{"request":request})

