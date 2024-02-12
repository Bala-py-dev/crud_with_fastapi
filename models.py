from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/sample_db"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Item(Base):
    __tablename__="items"
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, index=True)
    q = Column(String)

class ItemTbl(Base):
    __tablename__="items_tbl"
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, index=True)
    q = Column(String)