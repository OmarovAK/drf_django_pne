# Generated by Django 5.0 on 2023-12-14 15:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measurement',
            options={'verbose_name': 'Измерение датчика', 'verbose_name_plural': 'Измерения датчиков'},
        ),
        migrations.AlterModelOptions(
            name='sensor',
            options={'verbose_name': 'Датчик', 'verbose_name_plural': 'Датчики'},
        ),
        migrations.AlterField(
            model_name='measurement',
            name='date',
            field=models.DateTimeField(verbose_name='Дата и время'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensor', to='sensors.sensor', verbose_name='Датчик'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='temperature_value',
            field=models.IntegerField(verbose_name='Значение температуры'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание датчика'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название датчика'),
        ),
    ]
