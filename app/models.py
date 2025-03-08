from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=30)


class District(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="region")


class Shop(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    is_take_away = models.BooleanField(default=False)





