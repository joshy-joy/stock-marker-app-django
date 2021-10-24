from django.contrib import admin
from .models import BuyOrder, SellOrder, CompletedOrder

# Register your models here.
admin.site.register(BuyOrder)
admin.site.register(SellOrder)
admin.site.register(CompletedOrder)
