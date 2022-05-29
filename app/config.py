import os
from dotenv import load_dotenv

SQLALCHEMY_DATABASE_URI=os.getenv('DB_URI')
SQLALCHEMY_TRACK_MODIFICATIONS=False
SECRET_KEY=os.getenv('SECRET_KEY')
JWT_SECRET_KEY=os.getenv('SECRET_KEY')