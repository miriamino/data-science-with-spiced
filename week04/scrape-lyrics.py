import requests
import re
import os
import time
from bs4 import BeautifulSoup
import pandas as pd
from helper_functions import get_urls, get_lyrics, transform_name, get_lyricspages

# if not os.path.isfile('lyrics.csv'):
lyrics_df = pd.DataFrame(columns=["title", "artist", "lyrics"])
#     artists = []
# else:
#     lyrics_df = pd.read_csv('lyrics.csv')
#     artists = lyrics_df['artist'].unique()


# new_artist = input('Add artist: ')
# if not transform_name(new_artist) in map(transform_name, artists):
#     artists += [new_artist]
# else:
#     print('Artist already in database.')

artists = ['princess nokia']

for artist in artists:
    lyricspages =  get_lyricspages(artist)
    if lyricspages:
        urls = get_urls(transform_name(artist), lyricspages)
        counter = 0
        for url in urls:
            data = get_lyrics(url)
            if data:
                t = data[0].strip("[]")
                a = data[1].strip("[]")
                l = ' '.join(data[2])
                lyrics_df = lyrics_df.append({"title": t, "artist": a, "lyrics": l}, ignore_index=True)
                counter +=1
            else:
                pass
        print(f'Added {counter} songs by {artist}')

lyrics_df.to_csv('lyrics.csv')