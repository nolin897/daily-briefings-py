
# app/__init__.py

import os
from dotenv import load_dotenv

load_dotenv()

APP_ENV = os.getenv("APP_ENV", default="development") # use "production" on a remote server

#ugly filename but has a special role: it says that there's a python app inside this directory that helps us import functions