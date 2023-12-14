from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


class CustomAuthenticate(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):

        try:
            user = get_user_model().objects.get(
                Q(username__iexact=username) | Q(phone__iexact=username) | Q(email__iexact=username))
        except get_user_model().DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            get_user_model().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
