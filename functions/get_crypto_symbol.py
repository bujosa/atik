import requests

from functions.generate_slug import generate_slug

def get_crypto_symbol(crypto_name):
    slug = generate_slug(crypto_name)
    url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={slug}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if len(data) > 0:
            return data[0]['symbol']
    return ''