__author__ = 'hira'
import tweepy
import json

class TwitterClient(object):

    _CONSUMER_KEY = ''
    _CONSUMER_SECRET = ''
    _ACCESS_TOKEN = ''
    _ACCESS_TOKEN_SECRET = ''
    _api = None

    def __init__(self):
        with open('twitter_keys.json', 'r') as keys_file:
            keys = json.load(keys_file)

            self._CONSUMER_KEY = keys['CONSUMER_KEY']
            self._CONSUMER_SECRET = keys['CONSUMER_SECRET']
            self._ACCESS_TOKEN = keys['ACCESS_TOKEN']
            self._ACCESS_TOKEN_SECRET = keys['ACCESS_TOKEN_SECRET']

            print('Twitter client opened')

            auth = tweepy.OAuthHandler(self._CONSUMER_KEY, self._CONSUMER_SECRET)
            auth.set_access_token(self._ACCESS_TOKEN, self._ACCESS_TOKEN_SECRET)

            self._api = tweepy.API(auth)

    def post(self, text):
        print('tweet : ' + text)
        self._api.update_status(text)

    def post_with_date(self, text):
        from datetime import datetime
        import pytz
        now = datetime.now()
        now = pytz.utc.localize(now)
        now = now.astimezone(pytz.timezone('Asia/Tokyo'))
        now_str = now.strftime("%H:%M:%S")
        self.post(text + " at " + now_str)
