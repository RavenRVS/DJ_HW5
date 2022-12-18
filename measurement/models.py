from django.db import models
from PIL import Image

class Sensor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=256, verbose_name='Описание')


class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements',
                                  verbose_name='ИД датчика')
    temperature = models.FloatField(verbose_name='Значение температуры')
    created_at = models.DateField(verbose_name='Дата внесения записи', auto_now_add=True)
    image = models.ImageField(verbose_name='Изображение', null=True)

