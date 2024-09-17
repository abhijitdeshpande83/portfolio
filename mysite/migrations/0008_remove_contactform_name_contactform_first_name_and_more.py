# Generated by Django 4.1 on 2024-08-25 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_alter_contactform_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactform',
            name='name',
        ),
        migrations.AddField(
            model_name='contactform',
            name='first_name',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='contactform',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='email',
            field=models.CharField(max_length=30),
        ),
    ]
