# Generated by Django 5.1.1 on 2024-09-29 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0017_alter_experience_timeline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True, max_length=2500),
        ),
    ]
