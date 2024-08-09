import requests
from bs4 import BeautifulSoup



d = {
    'name': 'btnG',
}

d['name']


def show_atribute(url,attr):
    r = requests.get(url)
    markup = r.text
    soup = BeautifulSoup(markup,'html.parser')
    teg = soup.find(attrs=attr)
    return teg


print(f"""
    Упаковка пива Чернігівське Титан 8% 1 л х 12 шт: {show_atribute("https://rozetka.com.ua/chernigivske-4820034925461/p362480604/",{"class":"product-price__big"}).text}
    """)

