from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

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

@login_required(login_url='accounts:login')
def User_Profile(request):
    profile = Profile.objects.get(user_id=request.user.id)
    return render(request, 'accounts/profile.html', {'profile': profile})

@login_required(login_url='accounts:login')
def Update_Profile(request):
    if request.method == 'POST':
        formreg = UpdateRegForm(request.POST, instance=request.user)
        fromprof = UpdateProfForm(request.POST, instance=request.user.profile)
        if formreg and fromprof.is_valid():
            formreg.save()
            fromprof.save()
            messages.success(request, 'Update Successful!', extra_tags='success')
            return redirect('accounts:profile')
    else:
        formreg = UpdateRegForm(instance=request.user)
        fromprof = UpdateProfForm(instance=request.user.profile)
    context = {'formreg': formreg, 'fromprof': fromprof}
    return render(request, "accounts/update_profile.html", context)


@login_required(login_url='accounts:login')
def Change_Password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password1 = form.cleaned_data['new_password1']
            new_password2 = form.cleaned_data['new_password2']

            if not request.user.check_password(old_password):
                messages.error(request, 'رمز عبور قدیمی نادرست است.')
                return redirect('accounts:change-password')

            if new_password1 != new_password2:
                messages.error(request, 'رمزهای عبور جدید مطابقت ندارند.')
                return redirect('accounts:change-password')

            request.user.set_password(new_password1)
            request.user.save()

            update_session_auth_hash(request, request.user)

            messages.success(request, 'رمز عبور شما با موفقیت تغییر یافت.')
            return redirect('home:home')
    else:
        form = ChangePasswordForm()

    return render(request, 'accounts/change_password.html', {'form': form})