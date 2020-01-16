import unittest
from unittest.mock import Mock, patch
from saywhat import create_app
from saywhat.twitter import _create_api, fetch_tweets


@patch('tweepy.AppAuthHandler')
@patch('tweepy.API')
class TestCreateApi(unittest.TestCase):
    def test_no_api_key(self, MockAPI, MockAppAuthHandler):
        app = create_app({'API_KEY': None, 'API_SECRET_KEY': 'secret_key'})
        with app.app_context():
            with self.assertRaises(EnvironmentError):
                _create_api()

    def test_no_api_secret_key(self, MockAPI, MockAppAuthHandler):
        app = create_app({'API_KEY': 'mykey', 'API_SECRET_KEY': None})
        with app.app_context():
            with self.assertRaises(EnvironmentError):
                _create_api()


@patch('saywhat.twitter._create_api')
class TestFetchTweets(unittest.TestCase):
    def setUp(self):
        mock_user = Mock(name='user_obj', id='123', screen_name='realdonaldtrump')
        orig_tweet1 = Mock(
            name='orig_tweet',
            retweeted=False,
            id_str='456',
            created_at='today',
            user=mock_user,
            full_text='original tweet',
        )
        orig_tweet2 = Mock(
            name='orig_tweet',
            retweeted=False,
            id_str='456',
            created_at='today',
            user=mock_user,
            full_text='original tweet yoyoyo',
        )
        retweet1 = Mock(
            name='retweet1',
            retweeted=False,
            id_str='456',
            created_at='today',
            user=mock_user,
            full_text='RT @ retweet',
        )
        retweet2 = Mock(
            name='retweet2',
            retweeted=True,
            id_str='456',
            created_at='today',
            user=mock_user,
            full_text='retweet with retweeted attr',
        )

        patch_cursor = patch('tweepy.Cursor')
        self.mock_cursor = patch_cursor.start()
        self.mock_cursor.return_value.items.return_value = iter(
            [orig_tweet1, orig_tweet2, retweet1, retweet2]
        )
        self.addCleanup(patch_cursor.stop)

    def test_called_with_screen_name(self, mock_create_api):
        fetch_tweets(screen_name='realdonaldtrump')

        self.mock_cursor.assert_called_with(
            method=mock_create_api().user_timeline,
            screen_name='realdonaldtrump',
            tweet_mode='extended',
            include_rts=True,
        )

    def test_called_with_user_id(self, mock_create_api):
        fetch_tweets(user_id=25073877)

        self.mock_cursor.assert_called_with(
            method=mock_create_api().user_timeline,
            user_id=25073877,
            tweet_mode='extended',
            include_rts=True,
        )

    def test_ignores_retweets(self, mock_create_api):
        result = fetch_tweets(screen_name='realdonaldtrump')

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['text'], 'original tweet')

    def test_fetches_only_tweets_with_query(self, mock_create_api):
        result = fetch_tweets(screen_name='realdonaldtrump', query='yoyo')

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['text'], 'original tweet yoyoyo')


if __name__ == '__main__':
    unittest.main()
