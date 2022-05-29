"""
Flask app initialiser
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_cors import CORS

# Base directory
baseDir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_pyfile(f"{baseDir}/config.py")

db = SQLAlchemy(app)
CORS(app)
from app import models
db.create_all()

# Endpoints
from app import routes 
