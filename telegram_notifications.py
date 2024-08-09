import requests
from dotenv import dotenv_values

DOTENV = dotenv_values(".env")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{DOTENV['TELEGRAM_BOT_TOKEN']}/sendMessage"


def send_notification_about_price(product, price, url):
    text = f"""
            🛒 <b>Product Name:</b> {product}
            💵 <b>Price:</b> {price}
            🔗 <a href="{url}">Rozetka.ua</a>
            """
    request_data = {
        'chat_id': DOTENV['TELEGRAM_CHAT_ID'],
        'text': text,
        'parse_mode': "HTML"
    }
    response = requests.post(TELEGRAM_API_URL, data=request_data)
    status_code = response.status_code
    return status_code
