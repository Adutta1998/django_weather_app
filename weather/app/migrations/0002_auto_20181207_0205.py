# Generated by Django 2.1.4 on 2018-12-06 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weatherdata',
            name='air_speed',
        ),
        migrations.RemoveField(
            model_name='weatherdata',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='weatherdata',
            name='temp',
        ),
    ]