#Django imports
from django.shortcuts import render

#Python package imports

#REST_Framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions

#App import
from trade.models import BuyOrder, SellOrder
from trade.serializers import BuyOrderSerializer, SellOrderSerializer
from user.auth import UserAuthentication



class Tradebook(APIView):
    authentication_classes = [UserAuthentication]

    def get(self, request):
        try:
            buy = BuyOrder.objects.filter(symbol=request.data['symbol'])
            buy_serializer = BuyOrderSerializer(data=buy, many=True)
            buy_serializer.is_valid()
            sell = SellOrder.objects.filter(symbol=request.data['symbol'])
            sell_serializer = SellOrderSerializer(data=buy, many=True)
            sell_serializer.is_valid()
            return Response({ "buy":buy_serializer.data, "sell": sell_serializer.data }, status=status.HTTP_200_OK)
        except:
            return Response({ "error":"something went wrong" }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)