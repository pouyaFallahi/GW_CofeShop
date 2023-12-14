from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend, BaseBackend

from GW_CofeShop.coffe.models import User
from django.db.models import Q


class PhoneNumberBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):

        try:
            user = User.objects.get(Q(phone__exact=username) | Q(email__exact=username))

        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            User().set_password(password)
        else:
            if User.check_password(password) and self.user_can_authenticate(user):
                return User
