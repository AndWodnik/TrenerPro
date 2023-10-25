# Generated by Django 4.2.6 on 2023-10-18 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrenerApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='excercise',
            name='Type',
            field=models.CharField(choices=[('maszyna', 'Maszyna'), ('wolne', 'Wolny ciężar'), ('wymienne', 'Wymienne'), ('inny', 'Inny')], default='inny', max_length=30, verbose_name='Typ ćwiczenia'),
        ),
    ]