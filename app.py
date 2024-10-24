<<<<<<< HEAD
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/api/words', methods=['GET'])
def get_words():
    try:
        response = requests.get('https://ja.wikipedia.org/w/api.php?action=query&list=allpages&aplimit=100&format=json')
        response.raise_for_status()
        data = response.json()
        words = [page['title'] for page in data['query']['allpages']]
        return jsonify(words), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/api/words', methods=['GET'])
def get_words():
    try:
        response = requests.get('https://ja.wikipedia.org/w/api.php?action=query&list=allpages&aplimit=100&format=json')
        response.raise_for_status()
        data = response.json()
        words = [page['title'] for page in data['query']['allpages']]
        return jsonify(words), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 2769016d9e30db929aaa1a4e2c2095f741b9583b
