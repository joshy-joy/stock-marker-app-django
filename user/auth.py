from rest_framework.authtoken.models import Token
from rest_framework import authentication
from rest_framework import exceptions

class UserAuthentication(authentication.TokenAuthentication):
    def authenticate(self, request):
        key = request.data.get('user_id')
        if not key:
            return None

        try:
            user = Token.objects.get(key=key).user
        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed('Token authentication Failed. expect token in "user_id"')

        return (user, None)