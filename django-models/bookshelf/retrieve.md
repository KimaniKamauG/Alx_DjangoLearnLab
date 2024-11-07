# Retrieve the created book.

book = Book.objects.get(title='1984')
print(book.title, book.author, book.publication_year) # Expected output is '1984 George Orwell 1949'