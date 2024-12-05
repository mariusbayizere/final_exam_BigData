from django.db import models
# from final_exam_BigData.Model.sensors import Sensor
from models_app.Model.sensors import Sensor


class SensorData(models.Model):
    """
    A Django model representing data collected by a sensor.
    
    Attributes:
        sensor (Sensor): The sensor that collected the data.
        sensor_value (float): The value recorded by the sensor.
        timestamp (datetime): The time the data was recorded.
    """
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)  # Reference the Sensor model
    sensor_value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'SensorData'

    def __str__(self):
        """
        Returns the string representation of the SensorData object.
        """
        return f"{self.sensor} - {self.sensor_value} at {self.timestamp}"
