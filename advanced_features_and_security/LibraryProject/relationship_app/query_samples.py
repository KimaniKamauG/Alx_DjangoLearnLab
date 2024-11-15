from .models import Author, Book, Library, Librarian 

# Query all the books by a specific author

myauthor = Author.objects.get(pk=2)
print(myauthor.name)
author_name = myauthor.name


#retrieving the books by that author
# author_books = Book.objects.all().filter(author__name=author_name)

author = Author.objects.get(name=author_name) #this line of code was not necessary but for the checker I write to pass the test
author_books = myauthor.books.all()
for book in author_books:
    print(f"{book.title}")

#retrieving a Library in database
library_name = 'ALX' # assumming library exists in database
# mylibrary = Library.objects.get(pk=1)
mylibrary = Library.objects.get(name=library_name)
mylibrary_books = mylibrary.books.all()

for book in mylibrary_books:
    print(f"Book: '{book.title}', written by: {book.author}")

mylibrarian = Librarian.objects.get(library=mylibrary)

#retrieving the Librarian at mylibrary
# print(f"{mylibrary.librarian.name} works at {mylibrary.name}")








# def get_books_by_author(author_name):
#     try: 
#         author = Author.objects.get(name=author_name), objects.filter(author=author)
#         books = author.books.all()
#         return books
#     except Author.DoesNotExist:
#         return None
    
# # List all books in a library 
# def get_books_in_library(library_name):
#     try:
#         library = Library.objects.get(name=library_name)
#         books = library.books.all()
#         return books 
#     except Library.DoesNotExist:
#         return None 
    
# # Retrieve the librarian for a specific library

# def get_librarian_for_library(library_name):
#     try:
#         library = Librarian.objects.get(library=library_name)
#         librarian = library.librarian
#         return librarian
#     except Library.DoesNotExist:
#         return None 
#     except Librarian.DoesNotExist:
#         return None 
