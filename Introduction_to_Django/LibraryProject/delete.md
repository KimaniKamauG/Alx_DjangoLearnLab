# Delete the book instance 

book.delete()

# Try to retrieve all books to confirm there in none

books = Book.objects.all()
print(list(books)) # Expected output is an empty list : []