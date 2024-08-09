import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from telegram_notifications import send_notification_about_price

load_dotenv()

PRODUCT_NAME = 'Упаковка пива Чернігівське Титан 8% 1 л х 12 шт'


def show_atribute(url, attr):
    r = requests.get(url)
    markup = r.text
    soup = BeautifulSoup(markup, 'html.parser')
    tag = soup.find(attrs=attr)
    return tag


tag = show_atribute("https://rozetka.com.ua/chernigivske-4820034925461/p362480604/", {"class": "product-price__big"})
send_status_code = send_notification_about_price(PRODUCT_NAME, tag.text)

print(f"Упаковка пива Чернігівське Титан 8% 1 л х 12 шт: {tag.text}")
print(f"Send to telegram status code: {send_status_code}")
