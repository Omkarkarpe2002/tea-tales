# Generated by Django 5.0.4 on 2024-04-14 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_booktagline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='booktagline',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]