from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from libapp.models import Student
from libapp.forms import LoginForm, RegisterForm

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

    loginform = LoginForm()

    context_data = {
        'message': message,
        'error': error,
        'form': loginform
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

''' def auth(request):
    data = request.POST
    username, password = data['username'], data['password']

    slist = Student.objects.filter(username=username, password=password)
    if slist:
        # valid username and password
        student = slist[0]
        session = request.session
        session['username'] = student.username
        session['userid'] = student.id
        return HttpResponseRedirect(reverse('libapp:privatehome'))
    else:
        # invalid username or password
        return HttpResponseRedirect(reverse('libapp:home') + '?error=1') '''

def auth(request):
    data = request.POST
    loginform = LoginForm(data)
    username, password = data['username'], data['password']

    slist = Student.objects.filter(username=username, password=password)
    if slist:
        # valid username and password
        student = slist[0]
        session = request.session
        session['username'] = student.username
        session['userid'] = student.id
        return HttpResponseRedirect(reverse('libapp:privatehome'))
    else:
        # invalid username or password
        context_data = {
            'form': loginform,
            'error': 'Invalid username or password',
        }

        return render(request, 'libapp/home.html', context_data)

def login_form(request):
    context_data = {}

    if request.method == 'GET':
        # user wants to view the form
        loginform = LoginForm()
        context_data['form'] = loginform

        data = request.GET
        if 'success' in data:
            message = 'Registered successfully. Please Login'
        else:
            message = ''

        context_data['message'] = message
    else:
        # we assume it is POST
        # user wants to submit the same form
        data = request.POST # raw data coming from the client is always string
        loginform = LoginForm(data)
        context_data['form'] = loginform

        if loginform.is_valid():
            # true value when all the field validations pass `at the server side`

            # it does automatic type conversion of the raw data coming in the request
            # to whatever data type that was mentioned in the django form
            cleaned_data = loginform.cleaned_data
            # {'username': 'abc', 'password': '35345dfds'}

            slist = Student.objects.filter(**cleaned_data)
            if slist:
                # valid username and password
                student = slist[0]
                session = request.session
                session['username'] = student.username
                session['userid'] = student.id
                return HttpResponseRedirect(reverse('libapp:privatehome'))
            else:
                # invalid username or password
                context_data['error'] = 'Invalid username or password'
        ''' else:
            # false value when some field validation fails at the server side '''

    # 1. Invalid username or password
    # 2. When the user requests for the login page
    # 3. When the field validations fail at the server side
    return render(request, 'libapp/home.html', context_data)

def register_form(request):
    context_data = {}
    if request.method == 'GET':
        regform = RegisterForm()
        context_data['form'] = regform
    else:
        data = request.POST
        regform = RegisterForm(data)
        context_data['form'] = regform

        if regform.is_valid():
            cleaned_data = regform.cleaned_data
            s = Student(**cleaned_data)
            try:
                s.save()
            except Exception:
                context_data['error'] = 'Some error during registration'
            else:
                return HttpResponseRedirect(reverse('libapp:home') + '?success=1')

    return render(request, 'libapp/register.html', context_data)

class RegisterFormView(FormView):
    template_name = 'libapp/register.html'
    form_class = RegisterForm

    def form_valid(self, regform):
        cleaned_data = regform.cleaned_data
        s = Student(**cleaned_data)
        try:
            s.save()
        except Exception:
            context_data = {
                'error': 'Some error during registration',
                'form': regform
            }
            return render(self.request, 'libapp/register.html', context_data)
        else:
            return HttpResponseRedirect(reverse('libapp:home') + '?success=1')