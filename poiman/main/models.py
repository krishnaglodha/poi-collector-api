from django.contrib.gis.db import models

# Create your models here.

class aoipoints(models.Model):
    """
    Model of AOI Points.
    """
    name = models.CharField(max_length=50)
    geometry = models.PointField(srid=4326)

    # Returns the string representation of the model.
    def __str__(self):
        return self.name