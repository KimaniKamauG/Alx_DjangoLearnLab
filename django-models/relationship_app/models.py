from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver 

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} by {self.author}'
    
    class Meta:
        permissions = [('can_add_book', 'Can add a new book'),
         ('can_change_book', 'Can change a book'),
         ('can_delete_book', 'Can delete a book'),]
    
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='library')

    def __str__(self):
        return self.name 
    
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian' ),
    ('Member', 'Member'),
]
class UserProfile(models.Model):
    #class Roles(models.TextChoices):
     #   admin = "Admin"
      #  librarian = "Librarian"
       # member = "Member"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self) -> str:
        return f"{self.user.username}'s profile."
    
    # Signal to automatically create a UserProfile when a new user is created 
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()
 