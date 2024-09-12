from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def executar_curl():
    url = 'ipinfo.io' # Substitua pela URL desejada
    resposta = requests.get(url)
    return resposta.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)