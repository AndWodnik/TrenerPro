# Generated by Django 4.2.6 on 2023-10-19 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrenerApp', '0008_measurement_bfr_measurement_bodywater_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='Abdomen',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='Obwód brzucha w cm'),
        ),
        migrations.AddField(
            model_name='measurement',
            name='Chest',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='Klatka piersiowa cm'),
        ),
        migrations.AddField(
            model_name='measurement',
            name='Hips',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='Biodra w cm'),
        ),
        migrations.AddField(
            model_name='measurement',
            name='LeftArm',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name=' Lewe ramię w cm'),
        ),
        migrations.AddField(
            model_name='measurement',
            name='LeftThigh',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='Lewe udo w cm'),
        ),
        migrations.AddField(
            model_name='measurement',
            name='RightArm',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='Prawe ramię w cm'),
        ),
        migrations.AddField(
            model_name='measurement',
            name='RightThigh',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='Prawe udo w cm'),
        ),
        migrations.AddField(
            model_name='measurement',
            name='Waist',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='Talia w cm'),
        ),
    ]