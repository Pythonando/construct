from django.contrib import admin
from django.contrib.auth import admin as admin_auth_django

from .models import Users
from .forms import UserChangeForm, UserCreationForm


@admin.register(Users)
class UsersAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ('Cargo', {'fields': ('cargo',)}),
    )

