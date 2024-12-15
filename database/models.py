
from pydantic import BaseModel


class LoginItem(BaseModel):
    email:str
    password:str

class UserItem(BaseModel):
    user_full_name:str
    user_email:str
    user_password:str

