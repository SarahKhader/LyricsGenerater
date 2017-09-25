import requests
from bs4 import BeautifulSoup
import markovify
import SongsGetter


def get_lyrics(url):
    links = SongsGetter.get_songs(url)
    corpus = ''
    for link in links:
        formatted_sentence_list = []
        source_code = requests.get(link, allow_redirects=False)
        # just get the code, no headers or anything
        plain_text = source_code.text.encode('ascii', 'replace')
        # BeautifulSoup objects can be sorted through easy
        soup = BeautifulSoup(plain_text, 'html.parser')
        line = soup.findAll('div', {'class': 'lcontent'})
        line = str(line).replace('<br/>', '').replace('<i>', '').replace('</i>', '').replace(
            '<div class="lcontent">', '').replace('</div>', '').replace('<!-- 11130126 -->', '')
        formatted_sentence_list = line.splitlines()
        for song in formatted_sentence_list:
            for verse in song.split('\n'):
                corpus = corpus + str(verse) + "\n"

    text_model = markovify.NewlineText(str(corpus))
    for i in range(10):
        print(text_model.make_sentence())
        # print(text_model)


get_lyrics('https://www.lyricsondemand.com/t/taylorswiftlyrics/index.html')
