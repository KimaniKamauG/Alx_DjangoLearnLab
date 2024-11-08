from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView 

# Create your views here.

# Function based view for listing all the books.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based view for displaying library details.
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    
    def get_context_date(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context 