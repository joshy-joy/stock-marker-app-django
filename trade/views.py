#Django imports
from django.shortcuts import render

#Python package imports
from collections import OrderedDict

#REST_Framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions
from rest_framework_simplejwt.tokens import RefreshToken

#App import
from .models import BuyOrder, SellOrder
from .serializers import BuyOrderSerializer, SellOrderSerializer
from .task import stock_exchange
from user.auth import UserAuthentication



class Buy(APIView):
    authentication_classes = [UserAuthentication]

    def post(self, request):
        buy_order_serializer = BuyOrderSerializer(data=request.data)
        if buy_order_serializer.is_valid():
            buy_order_serializer.save()
            stock_exchange()
            return Response({'message': 'Order placed successfully'}, status=status.HTTP_200_OK)
        return Response(buy_order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

class Sell(APIView):
    authentication_classes = [UserAuthentication]

    def post(self, request):
        sell_order_serializer = SellOrderSerializer(data=request.data)
        if sell_order_serializer.is_valid():
            sell_order_serializer.save()
            stock_exchange()
            return Response({'message': 'Order placed successfully'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(sell_order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
