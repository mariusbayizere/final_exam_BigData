from django.db import models
from .sensors import Sensor

class Anomaly(models.Model):
    """
    A Django model representing an anomaly detected by a sensor.

    Attributes:
        sensor (Sensor): The sensor associated with the anomaly.
        timestamp (datetime): The timestamp when the anomaly was detected.
        anomaly_score (float): A score representing the severity of the anomaly.
        severity (str): The severity level of the anomaly; can be 'Low', 'Medium', or 'High'.
        description (str): Additional information about the anomaly.
    """
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    anomaly_score = models.FloatField()
    severity = models.CharField(max_length=50, choices=[
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ], blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'Anomaly'

    def __str__(self):
        """
        Returns the string representation of the Anomaly object, 
        indicating the sensor and timestamp of the anomaly detection.
        """
        return f"Anomaly detected for {self.sensor.sensor_name} at {self.timestamp}"