from django import forms
from django.contrib.auth.models import User
import re

# All our forms are a class
class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(max_length=10, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=10, widget=forms.PasswordInput)

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
        password2 = self.cleaned_data['confirm_password']

        if password != password2:
            raise forms.ValidationError("تکرار رمز عبور اشتباه است")

        if len(password) < 8:
            raise forms.ValidationError("رمز عبور باید حداقل ۸ کاراکتر باشد")

        if not re.findall('[A-Z]', password):
            raise forms.ValidationError("رمز عبور باید حداقل شامل یک حرف بزرگ باشد")

        if not re.findall('[0-9]', password):
            raise forms.ValidationError("رمز عبور باید حداقل شامل یک عدد باشد")

        if not re.findall('[!@#$%^&*(),.?":{}|<>]', password):
            raise forms.ValidationError("رمز عبور باید حداقل شامل یک کاراکتر خاص باشد")

        return password

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=10, widget=forms.PasswordInput)