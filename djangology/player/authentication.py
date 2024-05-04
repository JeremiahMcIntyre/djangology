from django.contrib.auth.backends import BaseBackend
from .models import Users

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = Users.objects.get(username=username)
            if user.password == password:
                return user
        except Users.DoesNotExist:
            return None

    def get_user(self, userId):
        try:
            return Users.objects.get(pk=userId)
        except Users.DoesNotExist:
            return None
