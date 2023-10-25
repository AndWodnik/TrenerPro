# Generated by Django 4.2.6 on 2023-10-25 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TrenerApp', '0023_module_fulldescription_alter_module_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TrenerApp.module')),
            ],
            options={
                'verbose_name': 'Połączenie Plan-moduł',
                'verbose_name_plural': 'Połączenia Plan-moduł',
            },
        ),
        migrations.CreateModel(
            name='TrainingPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nazwa treningu')),
                ('Type', models.CharField(choices=[('cardio', 'Cardio'), ('mobility', 'Mobility'), ('siłowy', 'Siłowy'), ('fbw', 'FBW')], default='Mobility', max_length=30, verbose_name='Typ treningu')),
                ('FullDescription', models.TextField(blank=True, null=True, verbose_name='Opis treningu')),
                ('Module', models.ManyToManyField(through='TrenerApp.TrainingModule', to='TrenerApp.module')),
            ],
            options={
                'verbose_name': 'Plan treningowy',
                'verbose_name_plural': 'Plany treningowe',
            },
        ),
        migrations.AddField(
            model_name='trainingmodule',
            name='Training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TrenerApp.trainingplan'),
        ),
    ]