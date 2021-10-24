from django.urls import path

from . import views

urlpatterns = [
    path('', views.Tradebook.as_view(), name="tradebook"),
]