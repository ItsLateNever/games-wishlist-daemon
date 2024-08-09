import requests
from bs4 import BeautifulSoup
from telegram_notifications import send_notification_about_price
from utils import read_data

PRODUCT_NAME = 'Упаковка пива Чернігівське Титан 8% 1 л х 12 шт'
DATA = read_data()


def show_atribute(url, attr):
    r = requests.get(url)
    markup = r.text
    soup = BeautifulSoup(markup, 'html.parser')
    tag = soup.find(attrs=attr)
    return tag


def print_parsed_price(product_name, product_price):
    print(f'{product_name}: {product_price}')


for item in DATA:
    tag = show_atribute(item['url'], {item['className']: item['classValue']})
    send_status_code = send_notification_about_price(item['name'], tag.text, item['url'])
    print_parsed_price(item['name'], tag.text)
