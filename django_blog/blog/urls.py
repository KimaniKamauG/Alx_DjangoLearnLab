from django.urls import path 
from . import views 

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('home/', views.home_view, name='home'),

    path('post/', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),

    path('comment/', views.CommentListView.as_view(),name='comment-list'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(),name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(),name='comment-delete'),
    path('post/<int:pk>/comments/new/', views.commentdummy, name='comment-dummy'),

    path('tags/<tag_name>/', views.tag_view, name='post-tag'),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='post-tag_list'),
    path('search/', views.search_view, name='post-search'),

]