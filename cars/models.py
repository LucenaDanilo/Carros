from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, null=True, blank=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=False, null=False)

    def __str__(self) -> str:
        return self.model  
