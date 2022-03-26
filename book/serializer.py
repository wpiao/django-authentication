from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'author', 'price', 'added_by', 'created_at', 'updated_at')
        model = Book
