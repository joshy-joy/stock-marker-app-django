from django.db import models

# Create your models here.
class Portfolio(models.Model):
    user_id = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.symbol