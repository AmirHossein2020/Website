# Generated by Django 4.2.6 on 2025-04-19 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_special_itmes_imge'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe',
            name='location',
            field=models.TextField(null=True),
        ),
    ]
