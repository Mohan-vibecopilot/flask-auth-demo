import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

class Config:
    # Updated connection format (add your actual password if needed)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://mohan2005:@localhost:5432/auth_demo')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-123')