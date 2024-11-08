from django.shortcuts import render, redirect 
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import login, logout 
from django.contrib.auth.decorators import login_required 
from django.contrib import messages 
from django.urls import reverse_lazy 
from django.views.generic import CreateView 

# Create your views here.

# Function based view for listing all the books.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based view for displaying library details.
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    
    def get_context_date(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context 
    
# User Registration view

# class SignUpView(CreateView):
#     form_class = UserCreationForm 
#     success_url = reverse_lazy('login')
#     template_name = 'registration/register.html'

# USING DJANGO USER CREATION FORM
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # Create a new user
            login(request, user) # Automatically login the user
            messages.success(request, 'Registration successful. You have now logged in.')
            return redirect('list_books')
        else:
            messages.error(request, 'Registration failed. Please try again.')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_ap/register.html', {'form': form})

# User Login View with Django Authentication Form
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user) # Login the user
            messages.success(request, 'Login is successful.')
            return redirect('list_books') # Redirect to the book list page.
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})



# Profile View
@login_required 
def profile(request):
    user = request.user # Get the user that's logged in.
    return render(request, 'relationship_app/profile.html', {'user': user})

# User Logout View
@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out of the system.")
    return render(request, 'relationship_app/logout.html')