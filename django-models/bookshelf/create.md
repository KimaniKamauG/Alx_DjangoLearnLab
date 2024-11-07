# Contains the creation of a book instance.
from bookshelf.models import Book

# Creating a book instance in python via the shell.
book = Book.objects.create(title='1984', author='George Orwell', publication_year=1949) 
print(book)  # Expected output '1984 by George Orwell (1949)'