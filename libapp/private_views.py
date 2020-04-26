from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from libapp.models import Book

''' def show_home(request):
    # blist = Book.objects.all()
    blist = Book.objects.order_by('-price')
    session = request.session
    # url protection from non logged in access
    if 'username' not in session:
        return HttpResponseRedirect(reverse('libapp:home'))
    username = session['username']
    context_data = {
        'books': blist,
        'username': username
    }
    return render(request, 'libapp/private/home.html', context_data) '''

def show_home(request):
    # blist = Book.objects.all()
    blist = Book.objects.order_by('-price')
    session = request.session
    # url protection from non logged in access
    if 'username' not in session:
        return HttpResponseRedirect(reverse('libapp:home'))
    username = session['username']
    userid = session['userid']

    for book in blist:
        students = book.students.all()
        for student in students:
            if student.id == userid:
                book.is_issued = True # is_issued - derived property put in the django model
                break
        else:
            book.is_issued = False
            if book.no_of_copies == len(students):
                book.cannot_issue = True
            else:
                book.cannot_issue = False

    context_data = {
        'books': blist,
        'username': username
    }
    return render(request, 'libapp/private/home.html', context_data)

def show_book(request, bookid):
    book = Book.objects.get(id=bookid)
    session = request.session
    if 'username' not in session:
        return HttpResponseRedirect(reverse('libapp:home'))

    username = session['username']
    context_data = {
        'book': book,
        'username': username
    }
    return render(request, 'libapp/private/book-details.html', context_data)

def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('libapp:home'))

def return_book(request, bookid):
    session = request.session
    if 'username' not in session:
        return HttpResponseRedirect(reverse('libapp:home'))
    
    userid = session['userid']
    book = Book.objects.get(id=bookid)
    book.students.remove(userid)

    return HttpResponseRedirect(reverse('libapp:privatehome'))

    