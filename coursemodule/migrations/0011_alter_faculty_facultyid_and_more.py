# Generated by Django 5.0 on 2024-03-09 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursemodule', '0010_alter_facultycourse_facultyid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='facultyid',
            field=models.CharField(unique=True, max_length=50),  # Adjust the max_length according to your requirements
        ),
        migrations.AlterField(
            model_name='facultycourse',
            name='facultyid',
            field=models.CharField(unique=True, max_length=50),  # Adjust the max_length according to your requirements
        ),
    ]