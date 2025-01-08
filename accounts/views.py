from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def Registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(username=data['username'],
                                     email=data['email'],
                                     password=data['password'],
                                     first_name=data['first_name'],
                                     last_name=data['last_name'])
            return redirect('home:home')

    else:
        form = RegisterForm()

    context = {'form': form}

    return render(request, 'accounts/registration.html', context)

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                user = authenticate(request, username=data['username'], password=data['password'])
            except:
                user = authenticate(request, username=User.objects.get(email=data['user']), password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('home:home')
    else:
        form = LoginForm(request.POST)
    context = {'form': form}
    return render(request, "accounts/login.html", context)

def Logout(request):
    logout(request)
    return redirect('home:home')
