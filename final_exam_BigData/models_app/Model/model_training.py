from django.db import models

class ModelTraining(models.Model):
    """
    A Django model representing the training metrics of a machine learning model.
    
    Attributes:
        training_timestamp (datetime): The timestamp when the model training was recorded.
        model_version (str): The version of the trained model.
        accuracy (float): The accuracy score of the model.
        precision (float): The precision score of the model.
        recall (float): The recall score of the model.
        description (str): Additional information about the model training.
    """
    
    training_timestamp = models.DateTimeField(auto_now_add=True)
    model_version = models.CharField(max_length=50)
    accuracy = models.FloatField()
    precision = models.FloatField()
    recall = models.FloatField()
    description = models.TextField()


    class Meta:
        db_table = 'ModelTraining'

    def __str__(self):
        """
        Returns the string representation of the ModelTraining object,
        which includes the model version.
        """
        return f"Model Training {self.model_version}"