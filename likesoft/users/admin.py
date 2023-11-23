from django import forms
from django.contrib import admin

from users.models import User


class ProfileAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')


@admin.register(User)
class Admin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email', 'date_joined',)
    list_per_page = 10
