import argparse
from datetime import datetime, timedelta
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError
from passlib.context import CryptContext
from pydantic import BaseModel
from typing import Optional

from backend.authentication import authenticate_user, create_access_token, get_user, validate_jwt_bearer, validate_jwt_cookie
from database.models import LoginItem, UserItem
from database.user import validate_user
import utilities.init
from utilities.config import config
from webserver.routes import jobs, users

# # Create ArgumentParser
# parser = argparse.ArgumentParser()

# # Define arguments
# parser.add_argument("--config", type=str, help="Name of the config file to be used. By default it picks .env file.", default=".env")

# # Parse arguments
# args = parser.parse_args()

utilities.init.startup('.env')

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")

app.include_router(users.router, prefix="", tags=["Users"])
app.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("login.html",{"request":request})


