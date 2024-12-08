from django.contrib.auth.forms import UserCreationForm 
from django import forms 
from django.contrib.auth.models import User 
from .models import Post, Comment, Tag 
from django.forms.widgets import Textarea
from taggit.forms import TagWidget


class RegistrationForm(UserCreationForm):
    ''' A form that extends the UserCreationForm to include an email field.'''
    email = forms.EmailField(required=True, help_text='Only valid emails allowed!')

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1','password2']

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        max_length=50,
        required=False,
        help_text='Add a new tag.',
        widget=TagWidget())
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

    # Automatically assign the author when creating a post.
    def save(self, commit=True):
        post = super().save(commit=False)
        tag = self.cleaned_data['tags']
        if tag:
            Tag.objects.create(name=tag, posts=post)
        if commit:
            post.save()
        return post 
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write your comment here...', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].required = True # Ensure content is empty

class SearchForm(forms.Form):
    to_search = forms.CharField(
        max_length=150,
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Search...',

            }
        ))
