from db import create_engine, User, Tweet, Base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

u = User(screen_name='hey')
t = Tweet(text='hey guys', tweet_id=123, user=u)

session.add(t)
session.commit()

