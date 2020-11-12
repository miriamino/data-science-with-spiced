import os
from pathlib import Path
import pymongo
from sqlalchemy import create_engine
import time
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

time.sleep(10)

pg = create_engine(f'postgres://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@postgres_container:5432/tweets')

client = pymongo.MongoClient('mongodb_container')
db = client.tweets

