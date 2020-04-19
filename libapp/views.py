from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def show_home(request):
    data = request.GET
    if 'success' in data:
        message = 'Registered successfully. Please Login'
    else:
        message = ''

    context_data = {
        'message': message
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

    # return render(request, 'libapp/home.html')
    return HttpResponseRedirect(reverse('libapp:home') + '?success=1')
    # redirect takes a url which it will send to the browser in the response for this request
    # i.e unlike render function which use to send html to the browser, redirect()
    # will send redirect url to the browser
    # browser on reading the url will make another request on the clients behalf to the url
