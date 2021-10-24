from django.urls import path

from . import views

urlpatterns = [
    path('buy/', views.Buy.as_view(), name="buy"),
    path('sell/', views.Sell.as_view(), name="sell"),
]