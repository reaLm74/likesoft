from rest_framework import serializers

from .models import Books


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id', 'title', 'pub_date', 'author', 'isbn')
