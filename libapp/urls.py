from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from libapp.views import show_home, show_register, save_user, auth, login_form, register_form,\
    RegisterFormView
from libapp.private_views import show_home as private_home, show_book, logout, return_book,\
    issue_book


# libmgmt/

app_name = 'libapp' # URL namespace

urlpatterns = [
    # path('home/', show_home, name="home"),
    path('home/', login_form, name='home'),
    # path('register/', show_register, name='register'),
    # path('register/', register_form, name='register'),
    path('register/', RegisterFormView.as_view(), name='register'),
    # path('reguser/', save_user, name='saveuser'),
    # path('reguser/', register_form, name='saveuser'),
    path('reguser/', RegisterFormView.as_view(), name='saveuser'),
    # path('auth/', auth, name='login'),
    path('auth/', login_form, name='login'),
    path('private/home/', private_home, name='privatehome'),
    path('private/book/<int:bookid>', show_book, name='bookdetails'),
    path('private/logout', logout, name='logout'),
    path('private/return-book/<int:bookid>', return_book, name='returnbook'),
    path('private/issue-book/<int:bookid>', issue_book, name='issuebook'),
    path('contact-us/', TemplateView.as_view(template_name='libapp/contact.html'), name='contactus')
]
