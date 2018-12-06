from django.db import models

# Create your models here.
class WeatherData(models.Model):
    city = models.CharField(max_length=30)
    def __str__(self):
        return self.city
