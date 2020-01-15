from flask import current_app
import tweepy


def _create_api():
    API_KEY = current_app.config['API_KEY']
    API_SECRET_KEY = current_app.config['API_SECRET_KEY']
    if API_KEY is None:
        raise EnvironmentError('API_KEY must be set.')
    if API_SECRET_KEY is None:
        raise EnvironmentError('API_SECRET_KEY must be set.')

    auth = tweepy.AppAuthHandler(API_KEY, API_SECRET_KEY)
    return tweepy.API(auth, wait_on_rate_limit=True)


def rate_limit_status():
    """Return rate limit status."""
    api = _create_api()
    status = api.rate_limit_status()
    return {
        'rate_limit_status': status['resources']['application'][
            '/application/rate_limit_status'
        ],
        'user_timeline': status['resources']['statuses']['/statuses/user_timeline'],
    }


def fetch_tweets(
    screen_name=None, user_id=None, keyword=None, since_id=None, limit=200
):
    """Fetch latest non-retweets from Twitter with optional keyword."""
    if screen_name is None and user_id is None:
        raise ValueError('Must provide a screen_name or user_id.')
    if keyword is None:
        keyword = ''

    api = _create_api()

    if screen_name:
        params = dict(
            method=api.user_timeline,
            screen_name=screen_name,
            tweet_mode='extended',
            include_rts=True,
        )
    else:
        params = dict(
            method=api.user_timeline,
            user_id=user_id,
            tweet_mode='extended',
            include_rts=True,
        )

    total = 0
    tweets = []
    for t in tweepy.Cursor(**params).items(limit):
        if (
            not t.retweeted
            and not t.full_text.startswith('RT @')
            and keyword.lower() in t.full_text.lower()
        ):
            tweets.append(
                {
                    'id': t.id_str,
                    'created_at': t.created_at,
                    'user_id': t.user.id,
                    'user_sname': t.user.screen_name,
                    'text': t.full_text,
                }
            )
        total += 1

    return tweets
