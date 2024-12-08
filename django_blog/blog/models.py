from django.db import models
from django.contrib.auth.models import User #get_user_model
from django.urls import reverse 
from taggit.managers import TaggableManager 


# User = get_user_model()
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    tags = models.TaggableManager(to='Tag', related_name='post_tag_set')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        """"""
        return reverse('post-detail', kwargs={'pk':self.pk})

    class Meta:
        ordering = ['title']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    posts = models.ManyToManyField(Post, related_name='post_tags')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post-tag', kwargs={'tag_name':self.name})
