from django.db import models

# Create your models here.
class Author(models.Model):
    '''
    Represents an author in the system.
    '''
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name 
    
class Book(models.Model):
    '''
    Represents a book written by the author.
    '''
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title 