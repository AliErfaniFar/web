from django import forms

# All our forms are a class
# تمامی فرم های ما یک class هستند و از forms.From ارثبری میکنند
class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(max_length=10)
    confirm_password = forms.CharField(max_length=10)