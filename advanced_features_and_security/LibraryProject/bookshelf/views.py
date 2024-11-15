from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Book

# Create your views here.
def index(request):
    return HttpResponse("Hello and welcome to my book app.")

def bookshop(request):
    all_books = Book.objects.all()
    template = loader.get_template('bookshelf/bookshop.html')
    context = {
        "all_books": all_books
    }
    #output = ','.join([q.title for q in all_books])
    return HttpResponse(template.render(context, request))