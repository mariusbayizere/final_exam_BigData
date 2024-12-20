from django.contrib import admin
from models_app.users import User
from models_app.sensors import Sensor
from models_app.sensor_data import SensorData
from models_app.model_training import ModelTraining


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'created_at')
    search_fields = ('username', 'role')

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('sensor_name', 'sensor_type', 'location')
    search_fields = ('sensor_name', 'sensor_type', 'location')

@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'sensor_value', 'timestamp')
    list_filter = ('sensor', 'timestamp')

@admin.register(ModelTraining)
class ModelTrainingAdmin(admin.ModelAdmin):
    list_display = ('model_version', 'accuracy', 'precision', 'recall', 'training_timestamp')
    list_filter = ('training_timestamp',)
