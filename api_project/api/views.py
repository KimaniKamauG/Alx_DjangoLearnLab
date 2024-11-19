from django.shortcuts import render
from rest_framework import generics 
from .serializers import BookSerializer 
from .models import Book 
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response 

# Create your views here.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 

class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view.

    def get(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data) 
