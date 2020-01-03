import json
import os
from pprint import pprint
import tweepy


def print_rls(api):
    """Print rate limit status."""
    status = api.rate_limit_status()
    print(
        'rate_limit_status:',
        status['resources']['application']['/application/rate_limit_status'],
    )
    print('user_timeline:', status['resources']['statuses']['/statuses/user_timeline'])

def get_api():
    API_KEY = os.getenv('API_KEY')
    API_SECRET_KEY = os.getenv('API_SECRET_KEY')

    auth = tweepy.AppAuthHandler(API_KEY, API_SECRET_KEY)
    api = tweepy.API(auth, wait_on_rate_limit=True)

def main():
    api = get_api()

    screen_name = 'realDonaldTrump'
    keyword = 'fair'

    tweets = []
    total = 0
    for t in tweepy.Cursor(api.user_timeline, tweet_mode='extended', screen_name=screen_name, include_rts=True, count=200).items(200):
        if not t.retweeted and not t.full_text.startswith('RT @') and keyword.lower() in t.full_text.lower():
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

    for t in tweets:
        pprint(t)
    print('Total tweets:', total)
    print('Total non-retweets:', len(tweets))

    #print_rls(api)


if __name__ == '__main__':
    main()
