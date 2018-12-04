from django.db import models

# Create your models here.
class WeatherData(models.Model):
    city = models.CharField(max_length=30)
    temp = models.CharField(max_length=30)
    air_speed = models.CharField(max_length=30)
    desc = models.CharField(max_length=200)
    def __str__(self):
        return self.city
