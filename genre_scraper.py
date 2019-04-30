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
    
def extarct_genre_links(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    elems = soup.find_all('li', class_="areatop-genre-rank__genre-item")
    genres = []
    links = []
    for e in elems:
        if e.find('a') != None:
            genres.append(e.getText())
            links.append(e.find('a').get('href'))
    return dict(zip(genres, links))

def memo():
    """
    ほしい関数。
    ページ内のジャンル数の数を数えてくれる関数
    ジャンルの番号を指定すればそのジャンル名とそのリンク先のランキング上位の画像のリンクを返してくれる関数
    """

def random_ganre(url):
    """
    取得したURLのジャンルからランダムに９個のジャンルを選択する。
    その先の画像リンク先とジャンル名を返す
    """
    genre_dict = extarct_genre_links(url)
    genre_dict_rand = random.choice(genre_dict)