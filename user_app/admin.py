from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user_app.models import User

class UserModelAdmin(BaseUserAdmin):

    list_display = ["id", "email", "name", "tc", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ("User Credential", {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name", "tc"]}),
        ("Permissions", {"fields": ["is_admin", "is_active"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", "tc", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email", "id"]
    filter_horizontal = []


admin.site.register(User, UserModelAdmin)
