import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()
URI = os.getenv('DATABASE_URL').replace('postgre', 'postgresql')
print(URI)
SQLALCHEMY_DATABASE_URI=URI
SQLALCHEMY_TRACK_MODIFICATIONS=False
SECRET_KEY=os.getenv('SECRET_KEY')
JWT_SECRET_KEY=os.getenv('SECRET_KEY')
JWT_ACCESS_TOKEN_EXPIRES = False