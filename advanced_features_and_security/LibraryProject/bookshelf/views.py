from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Book
from .forms import BookForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.db import DatabaseError

# Create your views here.
def index(request):
    return HttpResponse("Hello and welcome to my book app.")

def bookshop(request):
    all_books = Book.objects.all()
    template = loader.get_template('bookshelf/bookshop.html')
    context = {
        "all_books": all_books
    }
    #output = ','.join([q.title for q in all_books])
    return HttpResponse(template.render(context, request))

# View for listing all books
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    try:
        books = Book.objects.all()
        return render(request, 'bookshelf/booklist.html', {'books': books})
    except DatabaseError:
        return HttpResponse('Error occurred while fetching the books.', status=500)
    
# View for creating a new book
@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('book_list')
            except DatabaseError:
                return HttpResponse('Error occurred while saving the book', status=500)
        else:
            form = BookForm()
        return render(request, 'bookshelf/book_form.html', {'form': form})
    
@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            try:
                form.save()
                return redirect('book_list')
            except DatabaseError:
                return HttpResponse('Error occurred while saving the book', status=500)
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form})

@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        try:
            book.delete()
            return redirect('book_list')
        except DatabaseError:
            return HttpResponse('Error occurred while deleting the book', status=500)
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})