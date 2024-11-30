from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly 
from .models import Book
from .serializers import BookSerializer 

# Create your views here.

# ListView: Retrieve all books 
class BookListView(generics.ListCreateAPIView):
    '''
    Handles retrieving all books.
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    permission_classes = [IsAuthenticatedOrReadOnly] # Read-only access to unauthenticated users 

# DetailView: Retrieve a single book 
class BookDetailView(generics.RetrieveAPIView):
    '''
    Handles retrieving a single book by it's id.
    Allows read-only access ti unauthenticated users.
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    permission_classes = [IsAuthenticatedOrReadOnly]

# CreateView: Create a new book 
class BookCreateView(generics.CreateAPIView):
    '''
    Handles creating a new book.
    Only authenticated users can create a new book. 
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    permission_classes = [IsAuthenticated]

# UpdateView: Update an existing book 
class BookUpdateView(generics.UpdateAPIView):
    '''
    Handles updating an existing book.
    Only authenticated users can update books.
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    permission_classes = [IsAuthenticated]

# DeleteView: Delete an existing book 
class BookDeleteView(generics.DestroyAPIView):
    ''''
    Handles deleting a book.
    Only authenticated users can delete books.
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    permission_classes = [IsAuthenticated]



