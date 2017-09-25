import requests
from bs4 import BeautifulSoup
import SongsGetter


def get_lyrics(url):
    links = SongsGetter.get_songs(url)
    for link in links:
        source_code = requests.get(link, allow_redirects=False)
        # just get the code, no headers or anything
        plain_text = source_code.text.encode('ascii', 'replace')
        # BeautifulSoup objects can be sorted through easy
        soup = BeautifulSoup(plain_text, 'html.parser')
        for line in soup.findAll('div', {'class': 'lcontent'}):
            line = str(line).replace('<br/>', '').replace('<i>', '').replace('</i>', '').replace(
                '<div class="lcontent">', '').replace('</div>', '').replace('<!-- 11130126 -->', '')
            print(line)


get_lyrics('https://www.lyricsondemand.com/t/taylorswiftlyrics/index.html')
