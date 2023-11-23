from django import forms
from django.contrib import admin

from .models import Books


class ProfileAdminForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ('title', 'author', 'pub_date', 'isbn',)


@admin.register(Books)
class Admin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'author', 'pub_date', 'isbn',)
    list_per_page = 10
