from django.shortcuts import render


# The view related to the home page
def home(request):
    return render(request, 'home/home.html') # received the home.html page and in response to displays request
