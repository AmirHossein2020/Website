# Generated by Django 4.2.6 on 2024-04-02 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progarmmer', '0008_alter_resume_language_persian_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abuot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('title_persian', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('body_persian', models.TextField()),
            ],
        ),
    ]