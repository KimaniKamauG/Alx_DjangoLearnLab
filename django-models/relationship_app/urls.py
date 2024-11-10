from django.urls import path
from .views import list_books, LibraryDetailView 
from django.contrib.auth.views import LoginView, LogoutView
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', list_books, name='list_books'), # Function based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), # Class based view
    path('register/', views.register.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('members/', views.member_view, name='members'),
    path('librarian/', views.librarian_view, name='librarian'),
    path('adminview/', views.admin_view, name='adminview'),
]