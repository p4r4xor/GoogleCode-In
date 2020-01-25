from os import path
from time import sleep
import requests
import json
from flask import Flask
from flask import render_template
from flask import request
from flask import send_file

api = "Your API here"

def news():
    linux = json.loads(requests.get("https://newsapi.org/v2/everything?q=Linux&apiKey="+api+"&sortBy=publishedAt&sources=google-news").text)['articles']
    android = json.loads(requests.get("https://newsapi.org/v2/everything?q=Android&apiKey="+api+"&sortBy=publishedAt&sources=google-news").text)['articles']
    os = json.loads(requests.get("https://newsapi.org/v2/everything?q=Open-Source&apiKey="+api+"&sortBy=publishedAt&sources=google-news").text)['articles']
    return (linux, android, os)

app = Flask(__name__)
@app.route('/') 
def main():
    table = news()
    return render_template('index.html', linux=table[0], android=table[1], os=table[2])
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1337, debug=True)