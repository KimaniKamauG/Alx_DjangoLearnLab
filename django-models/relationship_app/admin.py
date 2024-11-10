from django.contrib import admin
from .models import Author, Book, Librarian, Library
# Register your models here.

# Define a custom admin class to control how models appear in the admin interface
class RelationAdmin(admin.ModelAdmin):
    # Customize the list display for the admin panel
    list_display = ('name',)  # Modify fields to match each model (e.g., 'title' for Book)
    search_fields = ('name',)  # Enable search by name
    list_filter = ('name',)  # Add filters to narrow down the list

# Register each model with the custom RelationAdmin class
@admin.register(Author)
class AuthorAdmin(RelationAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(RelationAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author__name')
    list_filter = ('author',)

@admin.register(Librarian)
class LibrarianAdmin(RelationAdmin):
    list_display = ('name', 'library')
    search_fields = ('name', 'library__name')
    list_filter = ('library',)

@admin.register(Library)
class LibraryAdmin(RelationAdmin):
    list_display = ('name',)
    search_fields = ('name', 'books')