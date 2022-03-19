from django.db import models


class Coin(models.Model):
    name = models.CharField(max_length=150)
    market_cap_rank = models.PositiveIntegerField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    current_price = models.FloatField(null=True, blank=True)
    high_24h = models.FloatField(null=True, blank=True)
    low_24h = models.FloatField(null=True, blank=True)
    price_change_24h = models.FloatField(null=True, blank=True)
    price_change_percentage_24h = models.FloatField(null=True, blank=True)
    market_cap_change_24h = models.FloatField(null=True, blank=True)
    market_cap_change_percentage_24h = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'coins'
