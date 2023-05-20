from flask import Flask, render_template, request, url_for, jsonify, redirect
import requests

app = Flask(__name__)


DEEZER_API_URL = 'https://api.deezer.com'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']

    response = requests.get(f'{DEEZER_API_URL}/search/artist?q={query}')
    artists = response.json()['data']

    # Render the search_results.html template and pass the artists data
    return render_template('search.html', artists=artists)


if __name__ == '__main__':
    app.run()
