from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'created_at')
    search_fields = ('username', 'role')

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('sensor_name', 'sensor_type', 'location')
    search_fields = ('sensor_name', 'sensor_type', 'location')

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('sensor_name', 'sensor_type', 'location')

@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'sensor_value', 'timestamp')
    list_filter = ('sensor', 'timestamp')

@admin.register(ModelTraining)
class ModelTrainingAdmin(admin.ModelAdmin):
    list_display = ('model_version', 'accuracy', 'precision', 'recall', 'training_timestamp')
    list_filter = ('training_timestamp',)

