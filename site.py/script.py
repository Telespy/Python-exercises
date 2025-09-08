from flask import Flask, render_template, request
import requests

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    movie = None
    error = None
    if request.method == 'POST':
        nome = request.form.get('nome_filme', '').strip()
        apikey = request.form.get('apikey', '').strip()
        if not nome or not apikey:
            error = 'Preencha nome do filme e API Key.'
        else:
            try:
                resp = requests.get('http://www.omdbapi.com/', params={'t': nome, 'apikey': apikey, 'r': 'json'}, timeout=6)
                resp.raise_for_status()
                data = resp.json()
                if data.get('Response', 'False') == 'True':
                    movie = data
                else:
                    movie = {}
                    error = data.get('Error', 'Filme não encontrado.')
            except requests.RequestException as e:
                error = f"Erro na requisição: {e}"
    return render_template('index.html', movie=movie, error=error)

if __name__ == '__main__':
    app.run(debug=True)