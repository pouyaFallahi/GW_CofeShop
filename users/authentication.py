from .models import CustomUser
from django.contrib.auth.backends import BaseBackend
from django.core.exceptions import ValidationError


class PhoneNumberBackend(BaseBackend):
    def authenticate(self, request, **kwargs):
        phone = kwargs.get('phone', None)
        password = kwargs.get('password', None)

        if not phone:
            raise ValidationError('Phone is required for authentication.')

        try:
            user = CustomUser.objects.get(phone=phone)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

        def get_user(self, user_id):
            try:
                return CustomUser.objects.get(pk=user_id)
            except CustomUser.DoesNotExist:
                return None
