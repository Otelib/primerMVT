from dataclasses import dataclass
from datetime import date
import os
from django.db import models
from django.forms import DateField
from datetime import datetime

# Create your models here.


class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    nacimiento = models.DateField(default=datetime.now)