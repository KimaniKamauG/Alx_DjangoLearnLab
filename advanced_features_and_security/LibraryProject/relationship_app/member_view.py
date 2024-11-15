from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .utils import check_role 


@user_passes_test(lambda user: check_role(user, 'Member'))
def member_view(request):
    return render(request, 'member_view.html', {'message': 'Welcome, Member'})