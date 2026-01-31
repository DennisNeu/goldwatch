from django.http import HttpResponse
from .key import key
import requests 

# Create your views here.

def index(request):
    return HttpResponse(get_gold_price())

def get_gold_price():
    api_key = key
    symbol = "XAU"
    curr = "EUR"
    date = ""

    url = f"https://www.goldapi.io/api/{symbol}/{curr}{date}"
    
    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return round(response.json()["price_gram_24k"], 2)
    except requests.exceptions.RequestException as e:
        print("Error:", str(e))
