# Generated by Django 5.0.1 on 2024-03-17 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_addblog_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addblog',
            name='type',
            field=models.CharField(max_length=255),
        ),
    ]
