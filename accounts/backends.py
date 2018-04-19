from django.contrib.auth.backends import ModelBackend as BaseModelBackend
from .models import User


class ModelBackend(BaseModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        if username is not None:
            try:
                user = User.objects.get(email=username)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                pass
