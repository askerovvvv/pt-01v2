from django.db import models

from account.models import CustomUser


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
    img = models.ImageField(upload_to='shop/')


class Saved(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="saveds")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="saveds")


