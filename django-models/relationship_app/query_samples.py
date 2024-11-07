from .models import Author, Book, Library, Librarian 

# Query all the books by a specific author
def get_books_by_author(author_name):
    try: 
        author = Author.objects.get(name=author_name), objects.filter(author=author)
        books = author.books.all()
        return books
    except Author.DoesNotExist:
        return None
    
# List all books in a library 
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books 
    except Library.DoesNotExist:
        return None 
    
# Retrieve the librarian for a specific library

def get_librarian_for_library(library_name):
    try:
        library = Librarian.objects.get(library=library_name)
        librarian = library.librarian
        return librarian
    except Library.DoesNotExist:
        return None 
    except Librarian.DoesNotExist:
        return None 
