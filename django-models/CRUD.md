Database Operations
CREATE Operation
from bookshelf.models import Book

Create a book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949) print(book)

RETRIEVE Operation
Retrieve the created book
book = Book.objects.get(title="1984") print(book.title, book.author, book.publication_year)

UPDATE Operation
Update the title of the book
book.title = "Nineteen Eighty-four" book.save()

Confirm the update
updated_book = Book.objects.get(id=book.id) print(updated_book.title)

DELETION Operation
Delete the book instance
book.delete()

Try to retrieve all books to confirm deletion
books = Book.objects.all() print(list(books))
