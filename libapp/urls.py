from django.contrib import admin
from django.urls import path
from libapp.views import show_home

# libmgmt/

urlpatterns = [
    path('home/', show_home)
]
