#Django imports
from django.shortcuts import render

#Python package imports

#REST_Framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User



class Register(APIView):

    def get(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        if username and password:
            try:
                user = User.objects.get(username = username)
                return Response(get_user_id(user))
            except:
                user = User.objects.create_user(username, password)
                user.save()
                return Response(get_user_id(user))
        return Response({'error': 'username and password fields are mandatory for id creation'}, status=status.HTTP_400_BAD_REQUEST)

def get_user_id(user_object):
    id = Token.objects.get_or_create(user=user_object)
    return {"id": str(id[0])}
