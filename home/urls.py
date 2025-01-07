from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [
    # Creating a url for the home page with the address 'None' and
    # rendering the view associated with the page
    path('', views.home, name='home'),
]
