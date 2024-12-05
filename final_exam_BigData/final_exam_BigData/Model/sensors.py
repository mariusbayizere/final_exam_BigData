from django.db import models

class Sensor(models.Model):
    """
    A Django model representing a Sensor with various attributes.
    
    Attributes:
        sensor_name (str): The name of the sensor.
        sensor_type (str, optional): The type of the sensor; can be blank or null.
        location (str, optional): The location of the sensor; can be blank or null.
        description (str, optional): Additional information about the sensor; can be blank or null.
    """
    sensor_name = models.CharField(max_length=255)
    sensor_type = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        """
        Returns the string representation of the Sensor object, which is the sensor's name.
        """
        return self.sensor_name