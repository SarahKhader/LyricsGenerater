import requests
from bs4 import BeautifulSoup


def get_songs(url):
    song_links = []
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    all_albums = soup.find('div', {'class': 'albmsnglst'})
    for name in all_albums.findAll('a'):
        name = name.string.replace(' ', '')
        href = 'https://www.lyricsondemand.com/t/taylorswiftlyrics/' + name + 'lyrics.html'
        song_links.append(href.lower())
    return song_links


