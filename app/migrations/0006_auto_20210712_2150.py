# Generated by Django 3.1.7 on 2021-07-13 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210710_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suscriptor',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='suscriptor',
            name='rut',
        ),
    ]
