import os
from sqlalchemy import create_engine, Column, DateTime, ForeignKey, Integer, relationship, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
DB = os.getenv('DB')

def User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    screen_name = Column(String)
    tweets = relationship('Tweet', back_populates='user', cascade='all, delete-orphan')


def Tweet(Base):
    __tablename__ = 'tweet'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    text = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='tweets')


if __name__ == '__main__':
    engine = create_engine(DB, echo=True)