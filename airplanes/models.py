from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Airplane(models.Model):
    tail_number = models.CharField(max_length=10, unique=True)
    model = models.CharField(max_length=100)
    capacity = models.IntegerField(validators=[MinValueValidator(1)])  
    production_year = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(timezone.now().year)]
    )
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.model} ({self.tail_number})"