# Generated by Django 5.1.4 on 2025-02-17 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_postal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
