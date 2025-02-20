from django import forms
from django.contrib.auth.models import User
import re
from .models import *

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("نام کاربری وجود دارد")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("ایمیل وارد شده تکراری است")
        return email

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password != confirm_password:
            raise forms.ValidationError("تکرار رمز عبور اشتباه است")

        if len(password) < 8:
            raise forms.ValidationError("رمز عبور باید حداقل ۸ کاراکتر باشد")

        if not re.findall('[A-Z]', password):
            raise forms.ValidationError("رمز عبور باید حداقل شامل یک حرف بزرگ باشد")

        if not re.findall('[0-9]', password):
            raise forms.ValidationError("رمز عبور باید حداقل شامل یک عدد باشد")

        if not re.findall('[!@#$%^&*(),.?":{}|<>]', password):
            raise forms.ValidationError("رمز عبور باید حداقل شامل یک کاراکتر خاص باشد")

        return confirm_password

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=10, widget=forms.PasswordInput)


class UpdateRegForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UpdateRegForm, self).__init__(*args, **kwargs)
        self.fields['username'].disabled = True


class UpdateProfForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender', 'address', 'phone', 'postal_code']

