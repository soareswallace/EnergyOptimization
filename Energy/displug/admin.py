from django.contrib import admin

from .models import Devices, Sensors

admin.site.register(Devices)
admin.site.register(Sensors)