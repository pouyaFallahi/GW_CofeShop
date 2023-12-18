from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class CustomAuthenticate(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = get_user_model().objects.get(
                Q(username__iexact=username) | Q(phone__iexact=username) | Q(email__iexact=username))
        except get_user_model().DoesNotExist:
            # Create a new user instance and set the password
            user = get_user_model()(
                username=username,
                email=username,  # You may need to adjust this based on your user model
            )
            user.set_password(password)
            user.save()

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
