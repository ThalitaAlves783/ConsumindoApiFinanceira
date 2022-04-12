from datetime import datetime

import requests as requests
import config

url_base ='https://hgbrasil.com/status/finance'.format('?key={0}', config.api_key)


def consultar_dados_financeiro(url):
    resposta = requests.get(url)
    dados = resposta.json()['results']['currencies']

    dolar = float(dados['USD']['buy'])
    euro = float(dados['EUR']['buy'])
    data_hora = str(datetime.now())

    from models.cotacao import Cotacao
    return Cotacao(dolar, euro, data_hora)


if __name__ == '__main__':
    dados = consultar_dados_financeiro(url_base)
    print(dados.__str__())

