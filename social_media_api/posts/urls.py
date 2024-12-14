from django.urls import path, include 
from .views import * #PostListView, PostCreateView, PostDetailView, PostDeleteView, PostUpdateView, PostSearchView, FeedView, LikePostView, UnlikePostView


urlpatterns = [
    
    path('posts/<int:pk>/comments/', PostListView.as_view(), name='post_detail'),
    path('posts/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/search/<slug:search_term>', PostSearchView.as_view(), name='post_search'),

    path('feed/', FeedView.as_view(), name='feed'),

    path('post/<int:pk>/comments/new', CommentCreateView.as_view(), name='comment_create'),
    path('post/<int:pk>/comments/', CommentListView.as_view(), name='comment_list'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete', CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),


    path('posts/<int:pk>/like/', LikePostView.as_view(), name='post_like'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='post_unlike'),

]

# urlpatterns += router.urls