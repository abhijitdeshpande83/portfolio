# Generated by Django 4.1 on 2024-08-24 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='certification_logo',
            field=models.ImageField(upload_to='media/certifications'),
        ),
        migrations.AlterField(
            model_name='tool',
            name='tool_logo',
            field=models.ImageField(upload_to='media/tools'),
        ),
    ]
