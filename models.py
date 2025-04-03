from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    username = Column(String)
    created_at = Column(DateTime)

class Device(Base):
    __tablename__ = 'devices'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    model = Column(String)
    screen_condition = Column(Boolean)
    body_condition = Column(Boolean)
    battery_condition = Column(Boolean)
    age = Column(Integer)
    estimated_price = Column(Float)
    created_at = Column(DateTime)

# Инициализация базы данных
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)