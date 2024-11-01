from django.contrib import admin
from .models import Book

# Register your models here
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    # Displays the title, author, and publication_year fields in the list view.
    list_filter = ("publication_year", "author")
    # Adds filter options by publication_year and author.
    search_fields = ("title", "author")
    # Enables a search bar to search by title and author