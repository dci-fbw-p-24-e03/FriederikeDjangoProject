from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUserProfile


class CustomUserAdmin(UserAdmin):
    """
    A custom user admin class to add custom fields to the user detail view.
    This custom class needs to be defined to make the custom fields of the
        CustomUserProfile visible and manageable in the admin interface.
    """

    # Add custom fields to the user detail view
    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {"fields": ("date_of_birth", "profession", "phone_number", "sex")},
        ),
    )

    # Add custom fields to the user creation form
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {"fields": ("date_of_birth", "profession", "phone_number", "sex")},
        ),
    )


admin.site.register(CustomUserProfile, UserAdmin)
