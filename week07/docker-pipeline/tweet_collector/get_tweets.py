import os
from pathlib import Path
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
import json
import logging
import pymongo

client = pymongo.MongoClient(host='mongodb_container', port=27017)
db = client.twitterdb
collection = db.tweets

def authenticate():
    """Function for handling Twitter Authentication. Please note
       that this script assumes you have a file called config.py
       which stores the 4 required authentication tokens:

       1. API_KEY
       2. API_SECRET
       3. ACCESS_TOKEN
       4. ACCESS_TOKEN_SECRET

    See course material for instructions on getting your own Twitter credentials.
    """
    auth = OAuthHandler(os.getenv('API_KEY'), os.getenv('API_SECRET'))
    auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))

    return auth

class TwitterListener(StreamListener):

    def on_data(self, data):

        """Whatever we put in this method defines what is done with
        every single tweet as it is intercepted in real-time"""

        t = json.loads(data) #t is just a regular python dictionary.

        # handling extended tweets
        text = t['text']
        if 'extended_tweet' in t:
            text = t['extended_tweet']['full_text']
        if 'retweeted_status' in t:
            r = t['retweeted_status']
            if 'extended_tweet' in r:
                text = r['extended_tweet']['full_text']

        tweet = {
        'text': text,
        'username': t['user']['screen_name'],
        'followers_count': t['user']['followers_count']
        }

        # logging.critical(f'\n\n\nTWEET INCOMING\n\n\n')
        collection.insert_one(tweet)
        # logging.critical(f'\n\n\nTWEET SAVED TO MONGODB: {tweet["text"]}\n\n\n')


    def on_error(self, status):

        if status == 420:
            print(status)
            return False



if __name__ == '__main__':

    auth = authenticate()
    listener = TwitterListener()
    stream = Stream(auth, listener)
    stream.filter(track=['feminist'], languages=['en'])