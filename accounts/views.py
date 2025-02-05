from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def Registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password'],
                first_name=data['first_name'],
                last_name=data['last_name']
            )
            messages.success(request, 'Registration Successful!', extra_tags='success')
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
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Login Successful!', extra_tags='success')
                return redirect('home:home')
            else:
                messages.error(request, 'Login Failed!', extra_tags='danger')
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, "accounts/login.html", context)

def Logout(request):
    logout(request)
    messages.success(request, 'Logout Successful!', extra_tags='primary')
    return redirect('home:home')

def Profile(request):
    return render(request, 'accounts/profile.html')