# Generated by Django 4.2.6 on 2024-04-02 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progarmmer', '0005_alter_resume_language_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='languages_persian',
        ),
    ]