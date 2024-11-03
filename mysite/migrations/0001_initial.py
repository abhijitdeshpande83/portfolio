# Generated by Django 5.1.1 on 2024-11-03 07:34

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('certification_id', models.AutoField(primary_key=True, serialize=False)),
                ('certification_rank', models.IntegerField(blank=True, default=99)),
                ('certification_name', models.CharField(default='', max_length=100)),
                ('certification_icon', models.FileField(default='', upload_to='certifications')),
                ('verification_url', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=15)),
                ('last_name', models.CharField(blank=True, default='', max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('message', models.TextField(blank=True, max_length=2500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(default='', max_length=50)),
                ('company_experience', models.TextField(blank=True, default='')),
                ('timeline', models.CharField(blank=True, default='', max_length=20)),
                ('role', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_name', models.CharField(blank=True, default='profile', max_length=20)),
                ('profile_pic', models.ImageField(blank=True, default='', upload_to='connectme')),
                ('resume_file_name', models.CharField(blank=True, default='resume', max_length=20)),
                ('resume_file', models.FileField(blank=True, default='', upload_to='cv')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_number', models.IntegerField()),
                ('column_number', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('skill_icon', models.FileField(default='', upload_to='skills')),
                ('description', models.TextField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('tool_id', models.AutoField(primary_key=True, serialize=False)),
                ('tool_rank', models.IntegerField(blank=True, default=99)),
                ('tool_name', models.CharField(default='', max_length=100)),
                ('tool_icon', models.FileField(default='', upload_to='tools')),
            ],
        ),
    ]
