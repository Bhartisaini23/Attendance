# Generated by Django 3.2.15 on 2022-11-03 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0003_alter_register_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='image',
            field=models.ImageField(default='', upload_to='face/images'),
        ),
    ]
