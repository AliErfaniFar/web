from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.shortcuts import redirect


# All our views are a function
# تمامی ویو های ما یک تابع هستند
def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(username=data['username'],
                                     first_name=data['first_name'],
                                     last_name=data['last_name'],
                                     email=data['email'],
                                     password=data['password'])

            return redirect('home:home') # app_name : name_in_url
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'accounts/registration.html', context)