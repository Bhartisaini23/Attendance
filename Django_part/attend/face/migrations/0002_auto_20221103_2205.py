# Generated by Django 3.2.15 on 2022-11-03 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='Student_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='register',
            name='phone',
            field=models.CharField(default='', max_length=50),
        ),
    ]