# Generated by Django 5.0.1 on 2024-03-17 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='typeofbook',
        ),
    ]
