from django.contrib import admin

from measurement.models import Sensor, Measurement


# Register your models here.
@admin.register(Sensor)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Measurement)
class TagAdmin(admin.ModelAdmin):
    pass
