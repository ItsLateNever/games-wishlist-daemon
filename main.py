import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.google.com.ua')
markup = r.text
soup = BeautifulSoup(markup,'html.parser')
teg = soup.find(attrs={'name':"btnG"})
print(teg.get("value"))