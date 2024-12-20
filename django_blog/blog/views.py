from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages 
from .forms import RegistrationForm, CommentForm, PostForm, SearchForm 
from django.contrib.auth.decorators import login_required 
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView 
from django.views.generic import TemplateView 
from django.urls import reverse_lazy, reverse 
from django.contrib.auth.models import User 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from .models import Post, Comment 
from django.http import HttpResponse, HttpResponseForbidden
from typing import Any 
from django.views import View 
from django.contrib.auth.decorators import login_required, user_passes_test 

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

# List View -Displays all posts 
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

# Detail View - Displays a single post 
class PostDetailView(DetailView):
    model = Post 
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# Create View - Allows creating a new post 
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
    
# Update View - Allows updating an existing post 
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post 
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 
    
# Delete View - Allows deleting a post 
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 


# Comments Section
class CommentCreateView(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    template_name = 'post_detail.html'
    model = Comment 

    def form_valid(self, form):
        '''
        Handles the valid form submission, saves the comment and redirects.
        '''
        if not self.request.user.is_authenticated:
            return HttpResponseForbidden('You must be logged in to comment.')
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post # Attaching the comment to the post.
        form.instance.author = self.request.user  # Attach the comment to the user.
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk']})
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_objects().post 
        return context 

class CommentListView(ListView):
    # A view to list all comments associated with a Post.
    model = Comment 
    template_name = 'blog/comment_list.html'
    context_object_name = 'comment_list'

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # A view for authenticated users to update their comments 
    model = Comment 
    template_name = 'blog/comment_update.html'
    fields = ['content']

    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().author
    
    def get_success_url(self) -> str:
        return reverse('post-detail', kwargs={'pk': self.get_object().post.pk})
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_object().post
        return context
    
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().author
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_object().post
        return context


class PostDetailCommentView(View):
    def get(self, request, *args, **kwargs):
        view = PostDetailView.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CommentCreateView.as_view()
        return view(request, *args, **kwargs)
    


@login_required
@user_passes_test
def dummy(request):
    if request.method == "POST":
        form = RegistrationForm(instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = RegistrationForm()

    return render(request, 'post_list.html', {'dummy':dummy})

def commentdummy(request, pk):
    return render(request, 'comment_create.html', {'dummy':dummy})



from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q


def search_view(request):
    queryset = Post.objects.all()
    form = SearchForm()

    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['to_search']
            searched_items = queryset.filter(Q(title__icontains=query)|Q(content__icontains=query))
        else:
            form = SearchForm()
    context = {
        'post_list': searched_items,
        'search_form': form,
    }
    return render(request, 'search.html', context=context)

def tag_view(request, tag_name):
    tag = get_object_or_404(klass=Tag, name__iexact=tag_name)
    post_by_tag = Post.objects.filter(Q(tags__name__icontains=tag.name))

    context = {
        'posts':post_by_tag,
        'tag_name':tag_name
    }

    return render(request, 'tags.html', context=context)

class PostByTagListView(ListView):
    model = Post
    template_name = 'tags.html'

