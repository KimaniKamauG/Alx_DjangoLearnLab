from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .utils import check_role 

@user_passes_test(lambda user: check_role(user, 'Librarian'))
def librarian_view(request):
    return render(request, 'librarian_view.html', {'message': 'Welcome, Librarian'})
