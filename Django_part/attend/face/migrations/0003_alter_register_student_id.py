# Generated by Django 3.2.15 on 2022-11-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0002_auto_20221103_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='Student_id',
            field=models.CharField(default='', max_length=50),
        ),
    ]
