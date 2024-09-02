from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.environ['DATABASE_CONN_URL']
engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()




class ScrapeHistory(Base):
    __tablename__ = "scraping_history"

    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)