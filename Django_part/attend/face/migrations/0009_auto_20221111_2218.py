# Generated by Django 3.2.15 on 2022-11-11 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0008_attendance_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='Student_name',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='register',
            name='id',
        ),
        migrations.AlterField(
            model_name='register',
            name='Student_id',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False),
        ),
    ]
