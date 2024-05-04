from django.contrib.auth.backends import BaseBackend
from .models import Users

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            print(f'Username is {username}')
            print(f'password is {password}')
            print(f'objects is {Users.objects}')
            user = Users.objects.get(username=username)
            print(f'Username: {user.username} Password:{user.password}')
            print(f'Check is {user.check_password(password)}')
            if user.password == password:
                return user
        except Users.DoesNotExist:
            return None

    def get_user(self, userId):
        try:
            return Users.objects.get(pk=userId)
        except Users.DoesNotExist:
            return None
