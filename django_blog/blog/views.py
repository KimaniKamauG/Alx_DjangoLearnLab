from django.shortcuts import render, redirect 
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages 
from .forms import RegistrationForm 
from django.contrib.auth.decorators import login_required 
from django.views.generic import CreateView 
from django.views.generic import TemplateView 
from django.urls import reverse_lazy 
from django.contrib.auth.models import User 

# Create your views here.

'''
This is the home view.
'''
def home_view(request):
    return render(request, 'blog/base.html')



'''
This is the registration view.
'''
class RegisterView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('profile') # Redirects to the home page.
    template_name = 'register.html'
    model = User 

    # def form_valid(self, form):
    #     form.save()
    #     login(self.request, user)
    #     return super().form_valid(form)
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Sign Up'
    #     return context 


# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('login')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'blog/register.html', {'form': form})


'''
This is the login view!
'''
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


'''
This is the logout view.
'''
def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after logging out.


'''
This is the Profile view and update.
'''
@login_required 
def profile(request):
    if request.method == 'POST':
        request.user.email = request.POST['email']  # Allow user to change email 
        request.user.save()
        return redirect('profile')
    return render(request, 'blog/profile.html')