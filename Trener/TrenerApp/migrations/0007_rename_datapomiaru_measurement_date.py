# Generated by Django 4.2.6 on 2023-10-19 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TrenerApp', '0006_measurement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='DataPomiaru',
            new_name='Date',
        ),
    ]
