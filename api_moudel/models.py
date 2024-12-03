from django.db import models

# Create your models here.

# The class "Data" represents a model with fields for an API key name, sensor name, and temperature.
class Data(models.Model):
    api_Key_Name = models.CharField(max_length=300)
    sensor_Name = models.TextField()
    temp = models.IntegerField(default=1)



    class Meta:
        db_table = 'acotechi_data'