import os
from django.db import models
from django.forms import DateField

# Create your models here.


class Familiar(models.Model):
    Nombre = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)
    Edad = models.IntegerField()