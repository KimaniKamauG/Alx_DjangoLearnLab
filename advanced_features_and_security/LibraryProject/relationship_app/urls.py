from django.urls import path
from .views import list_books, LibraryDetailView 
from django.contrib.auth.views import LoginView, LogoutView
from . import views 
from . import admin_view, librarian_view, member_view
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
    path('admin/', views.admin_view, name='admin_view'),
    path('admin/', admin_view.admin_view, name='admin_view'),
    path('librarian/', librarian_view.librarian_view, name='librarian_view'),
    path('member/', member_view.member_view, name='member_view'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>', views.delete_book, name='delete_book'),

]