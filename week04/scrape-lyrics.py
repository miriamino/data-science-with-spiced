import requests
import re
import os
import time
from bs4 import BeautifulSoup
import pandas as pd
from helper_functions import get_urls, get_lyrics, transform_name, get_lyricspages

if not os.path.isfile('lyrics.csv'):
    lyrics_df = pd.DataFrame(columns=["title", "artist", "lyrics"])
    artists = []
else:
    lyrics_df = pd.read_csv('lyrics.csv', index_col=0)
    artists = lyrics_df['artist'].unique()

new_artist = input('Add artist: ')
new_artist = new_artist.title()

if not new_artist in artists:
    artist = new_artist
    lyricspages =  get_lyricspages(artist)
    if lyricspages:
        urls = get_urls(transform_name(artist), lyricspages)
        counter = 0
        for url in urls:
            data = get_lyrics(url)
            if data:
                t = data[0]
                a = data[1]
                l = data[2]
                lyrics_df = lyrics_df.append({"title": t, "artist": a, "lyrics": l}, ignore_index=True)
                counter +=1
            else:
                pass
        print(f'Added {counter} songs by {artist}')
    lyrics_df.to_csv('lyrics.csv')
else:
    print('Artist already in database.')

