from django.urls import path
from . import views


app_name = ('accounts')
urlpatterns = [
    # Creating a url for the register page with the address 'registration' and
    # rendering the view associated with the page
    path('registration', views.Registration, name='registration'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
    path('profile', views.User_Profile, name='profile'),
]
