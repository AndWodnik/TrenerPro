# Generated by Django 4.2.6 on 2023-10-19 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrenerApp', '0004_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='FirstName',
            field=models.CharField(max_length=255, verbose_name='Imię'),
        ),
    ]