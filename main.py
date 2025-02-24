import requests
import json
from flask import Flask


def get_valutes_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    valutes = list(data['Valute'].values())
    return valutes


app = Flask(__name__)


def create_html(valutes):
    text = '<h1>Курс валют[Changed]</h1>'
    text += '<table style="border: 1px solid black; border-collapse: collapse;">'

    # Заголовок таблицы
    text += '<tr>'
    for key in valutes[0].keys():
        text += f'<th style="border: 1px solid black; padding: 5px;">{key}</th>'
    text += '</tr>'

    # Данные таблицы
    for valute in valutes:
        text += '<tr>'
        for v in valute.values():
            text += f'<td style="border: 1px solid black; padding: 5px;">{v}</td>'
        text += '</tr>'

    text += '</table>'
    return text


@app.route("/")
def index():
    valutes = get_valutes_list()
    html = create_html(valutes)
    return html


if __name__ == "__main__":
    app.run()