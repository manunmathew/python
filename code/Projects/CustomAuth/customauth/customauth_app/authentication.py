from django.contrib.auth.backends import BaseBackend
from customauth_app.models import User

class EmailBackend(BaseBackend):

    def authenticate(self,request,username =None, password = None, **kwargs):
        try:
            user_instance = User.objects.get(email=username)
            if user_instance.check_password(password):
                return user_instance
            else:
                return None
        except:
            return None

    def get_user(self, user_id):
        try:
            user_instance=User.objects.get(id=user_id)
            return user_instance
        except:
            return None


class PhoneBackend(BaseBackend):

    def authenticate(self, request, username = None, password = None, **kwargs):
        try:
            user_instance = User.objects.get(phone=username)
            if user_instance.check_password(password):
                return user_instance
            else:
                return None
        except:
            return None
    def get_user(self, user_id):
        try:
            user_instance=User.objects.get(id=user_id)
            return user_instance
        except:
            return None
