from django.urls import path
from measurement.views import Sensors, Sensor, Measurement


urlpatterns = [
    path('sensors/', Sensors.as_view()),
    path('sensors/<pk>/', Sensor.as_view()),
    path('measurements/', Measurement.as_view())
]
