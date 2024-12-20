"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView 
from django.views.generic import RedirectView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookshelf/', include('bookshelf.urls')),
    path('relationship_app/', include('relationship_app.urls')),
    path('accounts/', include('relationship_app.urls')),
    #path('', RedirectView.as_view(url='relationship/login/')),
    #path('accounts/profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
    #path('signup/', SignUpView.as_view(), name='templates/registration/signup')

]
