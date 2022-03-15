from django.db import models

# Create your models here.
from django.db.models import  BigAutoField

class StoreField(models.Model):

    year=models.IntegerField()
    duration=models.IntegerField()
    spends = models.FloatField()
    mode=models.TextField()
    purpose=models.TextField()
    quarter=models.TextField()
    country=models.TextField()
    prediction=models.IntegerField()

    def __repr__(self) -> str:
        return super().__repr__("Store value")

