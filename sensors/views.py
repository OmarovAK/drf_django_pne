from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView

from sensors.models import Sensor, Measurement
from sensors.serializer import SensorSerializer, MeasurementSerializer


class ListSensor(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class CreateSensor(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class UpdateSensor(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class CreateMeasurement(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class RetrieMeasurement(RetrieveAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
