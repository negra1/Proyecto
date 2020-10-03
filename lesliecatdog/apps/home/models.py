from django.db import models

# Create your models here.
class Home(models.Model):
    descripcion = models.CharField(max_length=200)
    Costo = models.IntegerField(default=0)