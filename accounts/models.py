from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(max_length=11, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    postal_code = models.IntegerField(max_length=10, blank=True, null=True)
    gender = models.CharField(max_length=15, choices=[('Male', 'Male'), ('Female', 'Female')], default='Male')

    def save_profile(sender, **kwargs):
        if kwargs['created']:
            profile_user = Profile(user=kwargs['instance'])
            profile_user.save()

    post_save.connect(save_profile, sender=User)