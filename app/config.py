import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS=False
SECRET_KEY=os.getenv('SECRET_KEY')
JWT_SECRET_KEY=os.getenv('SECRET_KEY')
JWT_ACCESS_TOKEN_EXPIRES = False