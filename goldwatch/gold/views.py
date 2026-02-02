from django.http import HttpResponse
from .key import key
from .models import GoldPurchase
import requests 
from decimal import Decimal

# Create your views here.
def index(request):
    gold_objects = GoldPurchase.objects.all()
    total_price = 0
    total_gold_in_grams = 0
    for x in gold_objects:
        total_gold_in_grams = total_gold_in_grams + x.amount_in_grams
        total_price = total_price + x.total_price_eur 
    current_gold_price = get_gold_price()
    print(total_price)
    print(total_gold_in_grams)
    print(current_gold_price)
    calculation = Decimal(current_gold_price) * Decimal(total_gold_in_grams) - total_price
    return HttpResponse(f"Your profit/loss is: {round(calculation, 2)} €")

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
