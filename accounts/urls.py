from django.urls import path
from . import views


app_name = ('accounts')
urlpatterns = [
    # Creating a url for the register page with the address 'registration' and
    # rendering the view associated with the page
    path('registration', views.registration, name='registration'),
]
