from django.db import models


# Create your models here.
class DhakaSubArea(models.Model):
    name = models.CharField(max_length=150, unique=True)
    bn_name = models.CharField(max_length=150)
    lat = models.FloatField(max_length=128)
    lng = models.FloatField(max_length=128)

    def __str__(self):
        return self.name
