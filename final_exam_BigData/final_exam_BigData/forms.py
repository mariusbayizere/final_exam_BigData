from django import forms
from .models import Sensor, ModelTraining

class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['sensor_name', 'sensor_type', 'location', 'description']


class SensorDataForm(forms.ModelForm):
    class Meta:
        model = SensorData
        fields = ['sensor', 'timestamp', 'sensor_value']
        widgets = {
            'timestamp': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ModelTrainingForm(forms.ModelForm):
    class Meta:
        model = ModelTraining
        fields = ['model_version', 'accuracy', 'precision', 'recall', 'description']

