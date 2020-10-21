import requests
import re
from bs4 import BeautifulSoup
import time

# todo the?
def transform_name(string):
    result = string.lower().replace(" ", "-")
    return result


def get_lyrics(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    lyrics = []
    verses = soup.find_all("p", class_="verse")
    verses = map(soup.get_text, verses)
    print(lyrics)
    if lyrics:
        artist = str(re.findall(r"lyrics-.*", url))
        artist = re.sub(r"lyrics-", "", artist)
        artist = re.sub(r".html", "", artist)
        artist = re.sub(r"-", " ", artist)
        artist = artist.title()
        title = str(re.findall(r".+-lyrics", url))
        title = re.sub(r"-lyrics", "", title)
        title = re.sub(r"https:\/\/www\.metrolyrics\.com\/", "", title)
        title = re.sub(r"-", " ", title)
        title = title.title()
        return [title, artist, lyrics]
    else:
        pass

print(get_lyrics('https://www.metrolyrics.com/saggy-denim-lyrics-princess-nokia.html'))

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


def get_lyricspages(artist):
    pages = []
    pgnum = 1
    lastpage = 0
    lyricspage = (
        f"https://www.metrolyrics.com/{transform_name(artist)}-alpage-{pgnum}.html"
    )
    if requests.get(lyricspage) != 404:
        while lastpage == 0:
            if re.match(r".*\d+", str(requests.get(lyricspage).url)) is not None:
                pages += [lyricspage]
                pgnum += 1
                lyricspage = f"https://www.metrolyrics.com/{transform_name(artist)}-alpage-{pgnum}.html"
                time.sleep(3)
            else:
                lastpage = 1
        return pages
    else:
        print(f"Ooops, can't find \"{artist}\", check spelling?")
        return False

# print(get_lyricspages('princess nokia'))