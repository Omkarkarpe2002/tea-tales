# Generated by Django 5.0.1 on 2024-04-01 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_booktagline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bookauthor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='bookrating',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='typeofbook',
            field=models.CharField(default='', max_length=50),
        ),
    ]
