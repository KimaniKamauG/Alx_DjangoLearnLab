from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .utils import check_role 

@user_passes_test(lambda user: check_role(user, 'Admin'))
def admin_view(request):
    return render(request, 'admin_view.html', {'message': 'Welcome, Admin'})

