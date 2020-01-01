import os
import tweepy


def main():
    API_KEY = os.getenv('API_KEY')
    API_SECRET_KEY = os.getenv('API_SECRET_KEY')

    auth = tweepy.AppAuthHandler(API_KEY, API_SECRET_KEY)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    username = 'realDonaldTrump'
    #id = api.get_user(username).id
    keyword = 'unfair'

    tweets = api.search(keyword+f' from:{username}')

    for t in tweets:
        print(t.text)




if __name__ == '__main__':
    main()