from django.db import models
from datetime import datetime


class Sensor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название датчика', unique=True)
    description = models.TextField(blank=True, verbose_name='Описание датчика')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensor', verbose_name='Датчик')
    temperature_value = models.IntegerField(verbose_name='Значение температуры')
    date = models.DateTimeField(verbose_name='Дата и время')

    def __str__(self):
        date = self.date
        return f'Температура для датчика {self.sensor} от {datetime.date(date).day}-{datetime.date(date).month}-{datetime.date(date).year} года'

    class Meta:
        ordering = ['date']
        verbose_name = 'Измерение датчика'
        verbose_name_plural = 'Измерения датчиков'
