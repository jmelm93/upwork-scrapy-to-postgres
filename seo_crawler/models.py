from pickletools import stringnl
from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, LargeBinary
    )
from sqlalchemy.engine.url import URL

# from settings import settings
# import settings

# from scrapy.utils.project import get_project_settings

DeclarativeBase = declarative_base()

DATABASE = {
    'drivername': 'postgresql',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',  
    'password': 'postgres',  
    'database': 'scrapy_testing'
}


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    # return create_engine(get_project_settings().get("CONNECTION_STRING"))
    return create_engine(URL(**DATABASE))
    # return create_engine(URL(**settings.DATABASE))


def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class ScrapyData(DeclarativeBase):

    __tablename__ = "scrapy_testing"

    id = Column(Integer, primary_key=True)
    crawl_date = Column(DateTime)
    download_time = Column(Integer)
    address = Column(String(200)) # https://www.pythonsheets.com/notes/python-sqlalchemy.html # CANT FIGURE OUT THIS DOUBLE PRECISION BS
    url_len = Column(Integer)
    domain = Column(String(200))
    path = Column(String(200))
    directories = Column(String(200))
    status_code = Column(Integer)
    robot = Column(String(200))
    canonical = Column(String(200))
    count_canonical = Column(Integer)
    content_type = Column(String(200))
    title = Column(String(200))
    count_title = Column(Integer)
    long_title = Column(String(200))
    missing_title = Column(String(200))
    description = Column(String(200))
    count_description = Column(Integer)
    keywords = Column(String(200))
    h1 = Column(String(200))
    count_h1 = Column(Integer)
    missing_h1 = Column(String(200))
    h2 = Column(String(200))
    count_h2 = Column(Integer)
    h3 = Column(String(200))
    count_h3 = Column(Integer)
    h4 = Column(String(200))
    count_h4 = Column(Integer)
    user_agent = Column(String(200))

 