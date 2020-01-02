import json
import os
import tweepy


def get_rl_status(api):
    status = api.rate_limit_status()
    print(
        'rate_limit_status:',
        status['resources']['application']['/application/rate_limit_status'],
    )
    print('user_timeline:', status['resources']['statuses']['/statuses/user_timeline'])


def main():
    API_KEY = os.getenv('API_KEY')
    API_SECRET_KEY = os.getenv('API_SECRET_KEY')

    auth = tweepy.AppAuthHandler(API_KEY, API_SECRET_KEY)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    # get_rl_status()

    sname = 'realDonaldTrump'
    keyword = 'unfair'

    """ for t in tweepy.Cursor(api.user_timeline, tweet_mode='extended', screen_name=sname).items(100):
        print(t.full_text)
 """


if __name__ == '__main__':
    main()
