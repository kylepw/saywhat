import os
import tweepy

API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')

def _create_api():
    if API_KEY is None:
        raise EnvironmentError('API_KEY must be set.')
    if API_SECRET_KEY is None:
        raise EnvironmentError('API_SECRET_KEY must be set.')

    auth = tweepy.AppAuthHandler(API_KEY, API_SECRET_KEY)
    return tweepy.API(auth, wait_on_rate_limit=True)

api = _create_api()


def rate_limit_status():
    """Print rate limit status."""
    status = api.rate_limit_status()
    print(
        'rate_limit_status:',
        status['resources']['application']['/application/rate_limit_status'],
    )
    print('user_timeline:', status['resources']['statuses']['/statuses/user_timeline'])

def fetch_tweets(screen_name=None, user_id=None, since_id=None, limit=200):
    """Fetch latest tweets from Twitter."""
    pass

def 


