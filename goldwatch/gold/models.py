from django.db import models

class GoldPurchase(models.Model):
    amount_in_grams = models.DecimalField(decimal_places=3)
    date = models.DateTimeField("date purchased")
    total_price_eur = models.DecimalField(decimal_places=2)