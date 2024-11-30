from django.db import models

# Create your models here.

# The Author model represents writers with a one-to-many relationship to books.
# The Book model includes details of a book and links back to the author who wrote it.


class Author(models.Model): 
    '''
    Represents and author in the database.
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 
class Book(models.Model):
    '''
    Represents a book in the database written by an author.
    '''
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title