from django.urls import path, include 
from rest_framework.routers import DefaultRouter 
from .views import BookList, BookViewSet 

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view 
    # Router for the BookViewSet (all CRUD Operations)
    path('', include(router.urls)),  # This includes all routes registered with the router 
]