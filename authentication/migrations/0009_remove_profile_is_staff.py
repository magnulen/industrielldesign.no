# Generated by Django 2.0.1 on 2019-03-12 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_profile_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_staff',
        ),
    ]
