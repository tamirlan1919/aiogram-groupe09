import requests
from bs4 import BeautifulSoup

def get_valutes():
    url = 'https://cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    dct = {}
    values = soup.find_all('Valute')
    for value in values:
        if value.CharCode.text in ['USD', 'EUR']:
            dct[value.CharCode.text] = {
                'value': value.Value.text,
            }


get_valutes()