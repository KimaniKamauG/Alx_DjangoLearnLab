# from django.urls import path 
# from .views import register, login
# from .views import AuthToken 
# from rest_framework.authtoken import views


# urlpatterns = [
#     path('register/', register, name='register'),
#     path('login/', login, name='login'),
#     #path('token/', AuthToken.as_view(), name='token'),
#     path('token/', views.obtain_auth_token),
# ]

from django.urls import path 
from rest_framework.authtoken import views
from .views import RegisterView, LoginView, ProfileView, follow_user, unfollow_user, CustomAuthToken


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('token/', CustomAuthToken.as_view(), name='token'),

    path('follow/<int:user_id>/', follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow_user'),
]