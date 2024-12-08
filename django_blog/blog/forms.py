from django.contrib.auth.forms import UserCreationForm 
from django import forms 
from django.contrib.auth.models import User 
from .models import Post, Comment 


class RegistrationForm(UserCreationForm):
    ''' A form that extends the UserCreationForm to include an email field.'''
    email = forms.EmailField(required=True, help_text='Only valid emails allowed!')

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1','password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    # Automatically assign the author when creating a post.
    def save(self, commit=True):
        post = super().save(commit=False)
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