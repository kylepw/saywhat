from sqlalchemy import create_engine, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    twitter_id = Column(Integer, nullable=False)
    screen_name = Column(String, nullable=False)
    tweets = relationship('Tweet', back_populates='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<User(id={self.id}, user_id={self.user_id}, screen_name={self.screen_name}, # of tweets: {len(self.tweets)})>'


class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(Integer, primary_key=True)
    tweet_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
    text = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='tweets')

    def __repr__(self):
        return f'<Tweet(id={self.id}, tweet_id={self.tweet_id}, created_at={self.created_at})>'