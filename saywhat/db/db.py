import os
from .models import Base, User, Tweet
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_PATH = os.getenv('DB_PATH')

def _create_session():
    if DB_PATH is None:
        raise EnvironmentError('DB_PATH must be set.')

    engine = create_engine(DB_PATH, echo=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    return Session()


session = _create_session()

def reset_tables():
    """Remove all rows from `tweets` and `users`tables."""
    session.query(Tweet).delete()
    session.query(User).delete()
    session.commit()

def add_tweets(tweets):
    pass

def get_tweets():
    pass

def count_tweets():
    pass

def search_tweets():
    pass

def last_tweet_id():
    pass

def get_users():
    pass

def search_users(twitter_id, screen_name):
    pass

def count_users():
    pass



if __name__ == '__main__':
    engine = create_engine(DB_PATH, echo=True)