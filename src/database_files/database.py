import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()


engine = create_engine(os.getenv("DATABASE_URL"), echo=False)


Base = declarative_base()


SessionLocal = sessionmaker(bind=engine)
