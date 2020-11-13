import requests
import os
import sqlalchemy as pg
import random
import time

webhook_url = os.getenv("WEBHOOK_URL")

pg_engine = pg.create_engine(f'postgres://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@postgres_container:5432/postgres')
connection = pg_engine.connect()

def get_data():
    query = """SELECT text, compound FROM tweets"""
    result = connection.execute(query)
    result = [{col: value for col, value in row.items()} for row in result]
    return result


def print_tweet(result):
    result = result
    rand = random.randint(0, len(result)-1)
    data = result[rand]
    print(data)
    

result = get_data()

while True:
    print_tweet(result)
    time.sleep(1)

# requests.post(url=webhook_url, json = data)

