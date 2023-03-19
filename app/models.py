from django.db import models

# Create your models here.
class RedZone(models.Model):
    location = models.CharField(null=True, max_length=100)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    title = models.CharField(null=True, max_length=500)
    cause = models.CharField(null=True, max_length=100)
    url = models.URLField(null=True)

    def __str__(self):
        return str(self.location)