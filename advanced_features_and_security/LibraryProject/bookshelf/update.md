# Updating the title of the book.

book.title = 'Nineteen Eighty-Four'
book.save()

# Confirming the update

updated_book = Book.objects.get(id=book.id)
print(updated_book.title) # Expected output is 'Nineteen Eighty-Four'