# Generated by Django 4.2.6 on 2023-10-19 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrenerApp', '0003_excercise_nameeng'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=255, verbose_name='ImiĘ')),
                ('SecondName', models.CharField(max_length=255, verbose_name='Nazwisko')),
                ('Email', models.CharField(max_length=255, verbose_name='e-mail')),
                ('PhoneNumber', models.CharField(max_length=255, verbose_name='Numer telefonu')),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'verbose_name': 'Osoba',
                'verbose_name_plural': 'Osoby',
            },
        ),
    ]
