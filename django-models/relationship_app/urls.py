from django.urls import path
from .views import list_books, LibraryDetailView, register_user, login_user, logout_user 

urlpatterns = [
    path('books/', list_books, name='list_books'), # Function based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), # Class based view
    path('register', register_user, name='register'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout')
]