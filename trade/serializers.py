from rest_framework import serializers

from .models import BuyOrder, SellOrder

class BuyOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyOrder
        fields = ('id', 'user_id', 'symbol', 'quantity', 'price')

class SellOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellOrder
        fields = ('id', 'user_id', 'symbol', 'quantity', 'price')