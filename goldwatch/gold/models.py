from django.db import models

class GoldPurchase(models.Model):
    amount_in_grams = models.DecimalField(decimal_places=3, max_digits=10)
    date = models.DateTimeField("date purchased")
    total_price_eur = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"This object documents the purchase of {self.amount_in_grams} for {self.total_price_eur}"