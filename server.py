# server.py
from flask import Flask, render_template
import os
import random
from modules import choice_shop

app = Flask(__name__)

@app.route('/')
def index():
    img_file_names = os.listdir('./static/img/')
    img_path_0 = "/static/img/" + random.choice(img_file_names)
    url = 'https://tabelog.com/tokyo/A1304/A130401/R7443/'
    genre_dict = choice_shop.get_genre_dict(url)
    genre_url, genre_nm = random.choice(list(genre_dict.items()))
    shop_dcit = choice_shop.get_shops_dict(genre_url)
    shop_url, shop_elem_dict = random.choice(list(shop_dcit.items()))
    return render_template('index.html', 
    img_path_0=img_path_0, 
    test_str=img_file_names,
    nm=shop_elem_dict['nm'],
    img_url=shop_elem_dict['img_url'],
    url=shop_url)
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=9000)
