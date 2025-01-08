from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User

def registration(request):
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