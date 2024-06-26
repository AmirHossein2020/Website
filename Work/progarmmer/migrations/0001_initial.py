# Generated by Django 4.2.6 on 2024-03-14 12:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameproject', models.CharField(max_length=50)),
                ('abuotproject', models.TextField(max_length=200)),
                ('photoproject', models.ImageField(upload_to='project/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experiencename', models.CharField(max_length=20)),
                ('aboutexperience', models.TextField(max_length=200)),
                ('startyear', models.DateField(default=django.utils.timezone.now)),
                ('endyear', models.DateField(default=django.utils.timezone.now)),
                ('nameinstitute', models.CharField(max_length=20)),
                ('startyear_education', models.DateField(default=django.utils.timezone.now)),
                ('endyear_education', models.DateField(default=django.utils.timezone.now)),
                ('namecity', models.CharField(default='null', max_length=20)),
                ('abuotinstitute', models.TextField(max_length=100)),
                ('professional_skill', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
            ],
        ),
    ]
