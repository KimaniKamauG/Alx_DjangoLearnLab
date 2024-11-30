from django.shortcuts import render
from rest_framework import generics, filters 
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated  
from .models import Book
from .serializers import BookSerializer 
from django_filters import rest_framework #as filters 
from django_filters.rest_framework import DjangoFilterBackend 

# Create your views here.

# ListView: Retrieve all books 
class BookListView(generics.ListCreateAPIView):
    '''
    Handles retrieving all books with advanced query capabilities.
    > Filtering by title, author, and publication_year
    > Searching by title and author's name
    > Ordering/Sorting by title and publication_year
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    permission_classes = [IsAuthenticatedOrReadOnly] # Read-only access to unauthenticated users 

    # Integrate filtering, searching and ordering.
    filter_backends = [
        DjangoFilterBackend, # For filtering 
        filters.SearchFilter, # For searching 
        filters.OrderingFilter, # For ordering 
    ]

    # Define the filter fields 
    filter_fields = [
        'title', # Filter by title
        'author', # Filter by author
        'publication_year', # Filter by publication year 
    ]

    # Define the search fields 
    search_fields = ['title', 'author__name'] # Use double underscores for related fields 

    # Define the ordering fields 
    ordering_fields = ['title', 'publication_year']
    ordering = ['title'] # Default ordering 




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



