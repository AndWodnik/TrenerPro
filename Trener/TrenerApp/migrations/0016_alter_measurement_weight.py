# Generated by Django 4.2.6 on 2023-10-24 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrenerApp', '0015_rename_muscles_excercise_directmus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='Weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Waga w kg'),
        ),
    ]