from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from libapp.models import Student

# Create your views here.

def show_home(request):
    data = request.GET
    if 'success' in data:
        message = 'Registered successfully. Please Login'
    else:
        message = ''

    if 'error' in data:
        error = 'Invalid username or password'
    else:
        error = ''

    context_data = {
        'message': message,
        'error': error
    }
    return render(request, 'libapp/home.html', context_data)

def show_register(request):
    return render(request, 'libapp/register.html')

def save_user(request):
    # collect the form data from the request
    data = request.POST
    username, password, country, gender = \
        data['username'], data['password'], data['country'], data['gender']
    
    # print(username, password, country, gender)
    # Save this data in a persistent store (database - MYSQL)
    s = Student(username=username, password=password, country=country, gender=gender)

    try:
        s.save()
    except Exception:
        return HttpResponse('Error in registration')
    else:
        return HttpResponseRedirect(reverse('libapp:home') + '?success=1')

    # return render(request, 'libapp/home.html')
    # redirect takes a url which it will send to the browser in the response for this request
    # i.e unlike render function which use to send html to the browser, redirect()
    # will send redirect url to the browser
    # browser on reading the url will make another request on the clients behalf to the url

def auth(request):
    data = request.POST
    username, password = data['username'], data['password']

    slist = Student.objects.filter(username=username, password=password)
    if slist:
        # valid username and password
        return HttpResponseRedirect(reverse('libapp:privatehome'))
    else:
        # invalid username or password
        return HttpResponseRedirect(reverse('libapp:home') + '?error=1')