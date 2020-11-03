import requests
import re
import os
import time
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
from pyfiglet import Figlet
from helper_functions import get_urls, get_lyrics, transform_name, get_lyricspages, transform_answer, clean_text
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
import spacy
from sklearn.ensemble import RandomForestClassifier
from imblearn.under_sampling import RandomUnderSampler, NearMiss
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, f1_score

nlp = spacy.load('en_core_web_md')


f = Figlet(font='cosmic')

if not os.path.isfile('lyrics.csv'):
    lyrics_df = pd.DataFrame(columns=["title", "artist", "lyrics"])
    artists = []
else:
    lyrics_df = pd.read_csv('lyrics.csv', index_col=0)
    artists = lyrics_df['artist'].unique()

print('You are using the lyrics bot. It guesses the artist of a song based on a line from the lyrics.\n')

screenreader = input('Are you using a screenreader with this programm? (y/n)   ')
screenreader = transform_answer(screenreader)
if screenreader == None:
    screenreader = input('I don\'t understand, did you mean y(es) or n(o)?    ')
    screenreader = transform_answer(screenreader)

add_artist = 1
while add_artist != 0:
    print(f'Artists in library {artists}')
    add_artist = input('Do you want to add an(other) artist to the lyrics library? (y/n)   ')

    add_artist = transform_answer(add_artist)
    if add_artist == None:
        add_artist = input('I don\'t understand, did you mean y(es) or n(o)?    ')
        add_artist = transform_answer(add_artist)

    if add_artist == 1:
        new_artist = input('Add artist: ')
        new_artist = new_artist.title()

        if not new_artist in artists:
            artist = new_artist
            if screenreader == 1:
                print('Downloading lyrics by {new_artist}...')
            else:
                print('Downloading lyrics by...')
                print(f.renderText(new_artist))
            lyricspages =  get_lyricspages(artist)


            if lyricspages:
                urls = get_urls(transform_name(artist), lyricspages)
                counter = 0
                for url in tqdm(urls):
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
            print(f'{new_artist} already in database.')

lyrics_df = pd.read_csv('lyrics.csv', index_col=0)

line = [input('Type a song line you want to identify: ')]
print('Calculating prediction...\n(yeah it\'s slow)')

lyrics_df = lyrics_df.dropna()

lyrics = lyrics_df['lyrics']
artists = lyrics_df['artist']

lyrics = lyrics.apply(clean_text, model=nlp)
vectorizer = TfidfVectorizer()
lyrics_v = vectorizer.fit_transform(lyrics)

bayes = MultinomialNB()
bayes.fit(lyrics_v, artists)

rf = RandomForestClassifier(n_estimators=20, max_depth=3, random_state=10)
rf.fit(lyrics_v, artists)

# rus = RandomUnderSampler(sampling_strategy='auto')
# nm = NearMiss(sampling_strategy='auto')
# L_rus, a_rus = rus.fit_resample(lyrics, artist)
# L_nm, a_nm = nm.fit_resample(lyrics, artist)

vline = bayes.predict(line)
wline = rf.predict(line) 
# if screenreader == 1:
#     print(f'The artist you\'re looking for is: (Bayes){vline} (Random Forest){wline}')
# else:
#     print('The artist you\'re looking for is:')
#     print(f.renderText(vline))
#     print(f.renderText(wline))
artists_predict_bayes = bayes.predict(artists)
artists_predict_rf = rf.predict(artists)

print(f'bayes: {vline}')
print(f'The accuracy of the model is: {round(accuracy_score(artists, artists_predict_bayes), 3)}')
print(f'The precision of the model is: {round(precision_score(artists, artists_predict_bayes), 3)}')
print(f'The recall of the model is: {round(recall_score(artists, artists_predict_bayes), 3)}')
print(f'The f1-score of the model is: {round(f1_score(artists, artists_predict_bayes), 3)}')
print(f'rf: {wline}')
print(f'The accuracy of the model is: {round(accuracy_score(artists, artists_predict_rf), 3)}')
print(f'The precision of the model is: {round(precision_score(artists, artists_predict_rf), 3)}')
print(f'The recall of the model is: {round(recall_score(artists, artists_predict_rf), 3)}')
print(f'The f1-score of the model is: {round(f1_score(artists, artists_predict_rf), 3)}')