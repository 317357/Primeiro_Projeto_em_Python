import json
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



requisicao = requests.get("https://economia.awesomeapi.com.br/all/USD-BRL")

cotacao = requisicao.json()

def escrever_json(cotacao):
    with open('meu_arquivo.json', 'w') as f:
        json.dump(cotacao, f)

def carregar_json(arquivo):
    with open('meu_arquivo.json', 'r') as f:
        return json.load(f)

minha_lista =['Moeda: ' + cotacao['USD']['name'],'Data: ' + cotacao['USD']['create_date'],'Valor atual: R$' + cotacao['USD']['bid']]


escrever_json(minha_lista)
