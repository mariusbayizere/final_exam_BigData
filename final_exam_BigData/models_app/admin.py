from django.contrib import admin
from .models import User, Sensor, SensorData, ModelTraining, Anomaly

admin.site.register(User)
admin.site.register(Sensor)
admin.site.register(SensorData)
admin.site.register(ModelTraining)
admin.site.register(Anomaly)
