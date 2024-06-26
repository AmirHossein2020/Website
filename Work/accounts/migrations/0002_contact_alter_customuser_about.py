# Generated by Django 4.2.6 on 2024-03-14 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='about',
            field=models.TextField(default='null', max_length=225),
        ),
    ]
