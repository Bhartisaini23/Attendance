# Generated by Django 3.2.15 on 2022-11-08 07:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0007_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='date'),
        ),
    ]