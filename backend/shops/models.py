from django.contrib.gis.db import models

class Shop(models.Model):
    name = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=5, decimal_places=2)
    lon = models.DecimalField(max_digits=5, decimal_places=2)
    geom  = models.PointField(srid=4326)
    geom_m = models.PointField(srid=26911)

    def __str__(self):
        return self.name

class ZipCodes(models.Model):
    ZIP = models.CharField(max_length=6)
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lon = models.DecimalField(max_digits=10, decimal_places=6)
    geom = models.PointField(srid=26911)

    def __str__(self) -> str:
        return f"{self.ZIP} {self.geom}"