import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv('./config/.secrets')
load_dotenv('app/config/.secrets')
sqlalchemy_url = os.getenv('SQLALCHEMY_DATABASE_URL')

engine = create_engine(
    sqlalchemy_url
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
