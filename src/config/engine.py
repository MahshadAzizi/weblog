from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging
from urllib.parse import quote_plus

from src.config.settings import DB

DBTYPE_POSTGRES = 'postgresql'

SQLALCHEMY_DATABASE_URL = '%s://%s:%s@%s:%s/%s' % (
    DBTYPE_POSTGRES, DB.user, quote_plus(DB.pass_), DB.host, DB.port, DB.name)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
