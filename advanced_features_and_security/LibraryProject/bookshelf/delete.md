# Deleting all the books created and confirming the deletion.
from bookshelf.models import Book

book.delete()

# Try to retrieve the book to confirm there is none.
books = Book.objects.all()
print(list(books)) # Expected output is an empty list []