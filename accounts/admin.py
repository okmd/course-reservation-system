from django.contrib import admin
from django.contrib.auth import models
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import RegistrationForm, ChangeForm



@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = RegistrationForm
    form = ChangeForm
    model = CustomUser
    list_display = ('email', 'is_active','is_superuser', 'is_staff','is_student')
    list_filter = ('email', 'is_active', 'is_student')
    fieldsets = (
        (None, {'fields': ('first_name','last_name','email', 'password', 'is_staff', 'is_student')}),
        ('Permissions', {'fields': ('is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2','is_active','is_staff', 'is_student')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)