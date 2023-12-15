from django.contrib import admin

from sensors.models import Sensor, Measurement


@admin.register(Sensor)
class AdminSensor(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


@admin.register(Measurement)
class AdminMeasurement(admin.ModelAdmin):
    list_display = ['id', 'sensor', 'temperature_value', 'date', ]
    list_filter = ['sensor', ]
