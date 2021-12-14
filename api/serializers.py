from rest_framework import serializers

from .models import Book

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'author', "description", "category", "addby")
        model = Book