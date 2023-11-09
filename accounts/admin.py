from django.contrib import admin  # type: ignore
from django.contrib.auth.admin import UserAdmin  # type: ignore

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "drobb2011@gmail.com",
        "username",
        "age",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                "fields": {
                    "age",
                }
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
