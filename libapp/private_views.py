from django.shortcuts import render
from libapp.models import Book

def show_home(request):
    # blist = Book.objects.all()
    blist = Book.objects.order_by('-price')
    context_data = {
        'books': blist
    }
    return render(request, 'libapp/private/home.html', context_data)
