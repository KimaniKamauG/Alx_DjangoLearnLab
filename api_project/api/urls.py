from django.urls import path, include 
from rest_framework.routers import DefaultRouter 
from .views import BookList, BookViewSet 
from rest_framework.authtoken.views import obtain_auth_token 

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view 
    # Router for the BookViewSet (all CRUD Operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
    # Url path for the Token Retrieval Endpoint 
    path('api-token-auth/', obtain_auth_token), 
]