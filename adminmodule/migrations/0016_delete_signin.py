# Generated by Django 5.0 on 2024-02-15 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0015_alter_signin_confirm_password_alter_signin_password_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Signin',
        ),
    ]