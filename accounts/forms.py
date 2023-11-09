from django.contrib.auth.forms import UserCreationForm, UserChangeForm  # type: ignore

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "drobb2011@gmail.com",
            "age",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "drobb2011@gmail.com",
            "age",
        )
