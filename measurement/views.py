from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from measurement.models import Sensor
from measurement.serializers import SensorSerializer, SensorDetailSerializer, CreateMeasurementSerializer


# Создать датчик. Указываются название и описание датчика.
# Получить список датчиков. Выдается список с краткой информацией по датчикам: ID, название и описание.
class Sensors(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# Изменить датчик. Указываются название и/или описание.
class Sensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# Добавить измерение. Указываются ID датчика и температура.
class Measurement(CreateAPIView):
    serializer_class = CreateMeasurementSerializer

