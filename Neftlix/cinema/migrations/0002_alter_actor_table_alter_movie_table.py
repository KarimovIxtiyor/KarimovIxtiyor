# Generated by Django 4.2.3 on 2023-07-11 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='actor',
            table='actor',
        ),
        migrations.AlterModelTable(
            name='movie',
            table='movie',
        ),
    ]
