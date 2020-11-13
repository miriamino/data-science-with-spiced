import os
from pathlib import Path
import pymongo
import sqlalchemy as pg
import time
import logging
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

time.sleep(10)

pg_engine = pg.create_engine(f'postgres://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@postgres_container:5432/postgres')
connection = pg_engine.connect()

meta = pg.MetaData()

etl_tweets = pg.Table(
  'tweets', meta,
  pg.Column('id', pg.String, primary_key = True),
  pg.Column('text', pg.String),
  pg.Column('username', pg.String),
  pg.Column('followers', pg.Integer),
  pg.Column('neg', pg.Float),
  pg.Column('neu', pg.Float),
  pg.Column('pos', pg.Float),
  pg.Column('compound', pg.Float)
)

meta.create_all(pg_engine)

client = pymongo.MongoClient(host='mongodb_container', port=27017)
db = client.twitterdb
collection = db.tweets


tweets = collection.find({})
s = SentimentIntensityAnalyzer()

def check_id(t):
    tw_id = str(t['_id'])
    id_query = f'SELECT EXISTS(SELECT 1 FROM tweets WHERE id LIKE \'{tw_id}\' );'
    result = connection.execute(id_query)
    result = [{col: value for col, value in row.items()} for row in result]
    return result[0]['exists']

def process_tweet(t):
    tw_id = str(t['_id'])
    text = t['text']
    user = t['username']
    followers = t['followers_count']
    sentiment = s.polarity_scores(text)
    neg = sentiment['neg']
    neu = sentiment['neu']
    pos = sentiment['pos']
    compound = sentiment['compound']
    insert_query = etl_tweets.insert().values(
        id = tw_id,
        text = text,
        username = user,
        followers = followers,
        neg = neg,
        neu = neu,
        pos = pos,
        compound = compound)
    connection.execute(insert_query)

while True:
    for t in tweets:
        if check_id(t) is False:
            process_tweet(t)
            time.sleep(100)