from django.contrib import admin
from django.urls import path
from libapp.views import show_home, show_register, save_user, auth
from libapp.private_views import show_home as private_home

# libmgmt/

app_name = 'libapp' # URL namespace

urlpatterns = [
    path('home/', show_home, name="home"),
    path('register/', show_register, name='register'),
    path('reguser/', save_user, name='saveuser'),
    path('auth/', auth, name='login'),
    path('private/home/', private_home, name='privatehome')
]
