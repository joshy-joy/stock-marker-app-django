#Django imports
from django.shortcuts import render

#Python package imports

#REST_Framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#App import
from portfolio.models import Portfolio
from .serializers import PortfolioSerializer
from user.auth import UserAuthentication



class PortfolioView(APIView):
    authentication_classes = [UserAuthentication]

    def get(self, request):
        portfolio = Portfolio.objects.filter(user_id=request.data['id'])
        portfolio_serializer = PortfolioSerializer(data=portfolio, many=True)
        portfolio_serializer.is_valid()
        return Response(portfolio_serializer.data)