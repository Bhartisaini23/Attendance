# Generated by Django 3.2.15 on 2022-11-12 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0009_auto_20221111_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='time',
            field=models.CharField(default='', max_length=50),
        ),
    ]
