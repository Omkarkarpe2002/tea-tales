# Generated by Django 5.0.1 on 2024-03-20 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_booktagline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='booktagline',
            field=models.CharField(default='', max_length=300),
        ),
    ]
