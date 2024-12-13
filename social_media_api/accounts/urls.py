from django.urls import path 
from .views import register, login
from .views import AuthToken 

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('token/', AuthToken.as_view(), name='token'),
]

