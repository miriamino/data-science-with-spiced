import requests
import re
from bs4 import BeautifulSoup
import time
import spacy

nlp = spacy.load('en_core_web_md')

# todo "the" band names?
def transform_name(string):
    result = string.lower().replace(" ", "-")
    return result

def transform_answer(string):
    if string == 'y' or string == 'yes':
        answer = 1
    elif string == 'n' or string == 'no':
        answer = 0
    else:
        answer = None
    return answer

def get_lyricspages(artist):
    pages = []
    pgnum = 1
    lyricspage0 = (
        f"https://www.metrolyrics.com/{transform_name(artist)}-lyrics.html"
    )
    lyricspage1 = (
        f"https://www.metrolyrics.com/{transform_name(artist)}-alpage-{pgnum}.html"
    )
    req0 = requests.get(lyricspage0)
    req1 = requests.get(lyricspage1)
    if req0.ok:
        while req0.text != req1.text:
            pages += [lyricspage1]
            pgnum += 1
            lyricspage1 = f"https://www.metrolyrics.com/{transform_name(artist)}-alpage-{pgnum}.html"
            req1 = requests.get(lyricspage1)
            time.sleep(3)           
        return pages
    else:
        print(f"Ooops, can't find \"{artist}\", check spelling?")


# todo check for doubles
def get_urls(artist, lyricspages):
    urls = []
    for lyricspage in lyricspages:
        page = requests.get(lyricspage)
        soup = BeautifulSoup(page.content, "lxml")
        new_urls = []
        for td in soup.find_all("td"):
            for a in td.find_all("a"):
                if artist in a.get("href"):
                    new_urls += [a.get("href")]
        urls += new_urls
        time.sleep(3)
    return urls


def get_lyrics(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    lyrics = []
    verses = soup.find_all("p", class_="verse")
    for v in verses:
        verse = v.get_text()
        verse = re.sub(r'\[.+\]', '', verse)
        lyrics += [verse]
    if lyrics:
        artist = str(re.findall(r"lyrics-.*", url))
        artist = re.sub(r"lyrics-", "", artist)
        artist = re.sub(r".html", "", artist)
        artist = re.sub(r"-", " ", artist)
        artist = artist.title().strip("['']")
        title = str(re.findall(r".+-lyrics", url))
        title = re.sub(r"-lyrics", "", title)
        title = re.sub(r"https:\/\/www\.metrolyrics\.com\/", "", title)
        title = re.sub(r"-", " ", title)
        title = title.title().strip("['']")
        lyrics = '\n'.join(lyrics)
        lyrics = lyrics.strip("[']")
        return title, artist, lyrics
    else:
        pass

def clean_text(review, model):
    new_doc = ''
    doc = model(review)
    for word in doc:
        if not word.is_stop and word.is_alpha:
            new_doc = f'{new_doc} {word.lemma_.lower()}'
    return new_doc