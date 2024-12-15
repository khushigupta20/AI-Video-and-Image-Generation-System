import dotenv
import os

class config:
    DBPATH = ""
    JWT_SECRET_KEY = "2428512ef29f155aca16e2353844cca6f98f84bc3571bef39242feb098282e5e"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30


def load_config(filename):
    dotenv.load_dotenv(filename)
    config.DBPATH = os.getenv("DBPATH")
