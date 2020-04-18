from django.shortcuts import render
# from django.http import HttpResponse
from datetime import datetime

def show_home(request):
    time = datetime.time(datetime.now())
    hour = time.hour

    if hour >= 0 and hour < 12:
        message = 'Good Morning'
    elif hour >= 12 and hour < 16:
        message = 'Good Afternoon'
    else:
        message = 'Good Evening'

    context_data = {
        'message': message
    }

    # return HttpResponse('<html><body>HelloWorld</body></html>')
    return render(request, 'home.html', context_data)

def show_contactus(request):
    return render(request, 'contactus.html')