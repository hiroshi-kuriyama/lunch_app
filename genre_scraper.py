import json
import requests
from bs4 import BeautifulSoup

url = 'https://tabelog.com/tokyo/'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

elems = soup.find_all('li', class_="areatop-genre-rank__genre-item")
genres = []
links = []
for e in elems:
    if e.find('a') != None:
        genres.append(e.getText())
        links.append(e.find('a').get('href'))
genre_link_dict = dict(zip(genres, links))
with open('./static/genres_data/tokyo_genres.json', mode='w') as f:
        json.dump(genre_link_dict, f)