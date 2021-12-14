from django.db import models
from rest_framework import generics, serializers
from .serializers import BooksSerializer 
from .models import Book

class Bookslistview(generics.ListCreateAPIView):
    serializer_class = BooksSerializer
    queryset = Book.objects.all()

class BooksDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BooksSerializer
    queryset= Book.objects.all()
