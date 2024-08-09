import requests
from dotenv import dotenv_values

DOTENV = dotenv_values(".env")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{DOTENV['TELEGRAM_BOT_TOKEN']}/sendMessage"


def send_notification_about_price(product, price):
    response = requests.post(TELEGRAM_API_URL,
                             data={'chat_id': DOTENV['TELEGRAM_CHAT_ID'], 'text': f'{product} - {price}'})
    status_code = response.status_code
    return status_code