from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



# PostgreSQL bazasiga ulanish uchun URL
#                         "postgresql://username:password@localhost/db_name"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1029@localhost/bfn1"

# Engine yaratish
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Sessiya yaratish
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base yaratish
Base = declarative_base()

# Sessiya ochish
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()