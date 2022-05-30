import os
from dotenv import load_dotenv
from datetime import timedelta

SQLALCHEMY_DATABASE_URI=os.getenv('DB_URI')
SQLALCHEMY_TRACK_MODIFICATIONS=False
SECRET_KEY=os.getenv('SECRET_KEY')
JWT_SECRET_KEY=os.getenv('SECRET_KEY')
JWT_ACCESS_TOKEN_EXPIRES = False