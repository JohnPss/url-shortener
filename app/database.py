from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import redis


SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost:5432/shortener_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
