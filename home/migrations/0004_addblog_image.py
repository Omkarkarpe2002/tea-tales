# Generated by Django 5.0.1 on 2024-03-15 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_addblog_author_alter_addblog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='addblog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog'),
        ),
    ]
