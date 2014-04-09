from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Title(models.Model):

	title_number = models.TextField()
	content = models.TextField()
	extent = models.GeometryField(srid=3857)

	objects = models.GeoManager()
