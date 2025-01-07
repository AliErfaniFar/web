from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # '''
    #     To create a superuser to enter the administration;
    #     First, enter the "python manage.py migrate" command,
    #     after performing the operation with the
    #     "python manage.py createsuperuser" command
    #     Create your own superuser.
    # '''
    path('admin/', admin.site.urls),

    # Introduction of home application and home urls
    path('', include('home.urls'), name='home'),

    # Introduction of accounts application and accounts urls
    path('', include('accounts.urls'), name='accounts'),
]
