from django.urls import path, include 
from .views import PostListView, PostCreateView, PostDetailView, PostDeleteView, PostUpdateView, PostSearchView, CommentViewSet
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('posts', PostListView)
# router.register('comments', CommentViewSet)


urlpatterns = [
    #path('', include(router.urls)),
    path('posts/<int:pk>/comments/', PostListView.as_view(), name='post_detail'),
    path('posts/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/search/<slug:search_term>', PostSearchView.as_view(), name='post_search'),


    path('comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),


]

# urlpatterns += router.urls