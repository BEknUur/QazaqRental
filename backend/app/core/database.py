from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

from app.core.base import Base  
engine = create_engine(settings.DATABASE_URL, connect_args={"sslmode": "require"})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
