import os
import requests
from dotenv import load_dotenv

def external_api_exchange(amount: str, from_currency: str) -> float:
    load_dotenv()
    api_key = os.getenv("API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_currency}&amount={amount}&apikey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        return round(response.json()['result'], 2)
    if response.status_code == 429:
        raise Exception('Too many requests for your subscription')
    else:
        raise ValueError(f"Failed to get currency rate")


# print(external_api_exchange("10", "USD"))