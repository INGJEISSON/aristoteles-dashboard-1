# Generated by Django 3.1.2 on 2021-01-22 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0003_auto_20201126_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
