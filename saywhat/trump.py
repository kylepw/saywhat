import json
import os
from pprint import pprint


def main():
    api = get_api()

    screen_name = 'realDonaldTrump'
    keyword = 'fair'

    tweets = []
    total = 0
    for t in tweepy.Cursor(
        api.user_timeline,
        tweet_mode='extended',
        screen_name=screen_name,
        include_rts=True,
        count=200,
    ).items(200):
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

    for t in tweets:
        pprint(t)
    print('Total tweets:', total)
    print('Total non-retweets:', len(tweets))

    # print_rls(api)


if __name__ == '__main__':
    main()
