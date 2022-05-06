from django.shortcuts import render
from .serializer import BookSerializer
from .models import Book
from rest_framework import generics


# Create your views here.
class ListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
