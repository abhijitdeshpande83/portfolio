# Generated by Django 4.1 on 2024-09-15 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_alter_contact_email_alter_contact_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(default='', max_length=50)),
                ('company_experience', models.CharField(default='', max_length=300)),
            ],
        ),
    ]
