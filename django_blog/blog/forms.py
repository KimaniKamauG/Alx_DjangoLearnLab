from django.contrib.auth.forms import UserCreationForm 
from django import forms 
from django.contrib.auth.models import User 


class RegistrationForm(UserCreationForm):
    ''' A form that extends the UserCreationForm to include an email field.'''
    email = forms.EmailField(required=True, help_text='Only valid emails allowed!')

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1','password2']