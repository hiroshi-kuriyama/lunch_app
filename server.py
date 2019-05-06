# server.py
from flask import Flask, render_template
import os
import random

app = Flask(__name__)

@app.route('/')
def index():
    img_file_names = os.listdir('./static/img/')
    img_path_0 = "/static/img/" + random.choice(img_file_names)
    test_str = 'aiueo'
    return render_template('index.html', img_path_0=img_path_0, test_str=img_file_names)
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=9000)
