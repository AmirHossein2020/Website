# Generated by Django 4.2.6 on 2024-08-26 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_remove_comment_about_comment_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]
