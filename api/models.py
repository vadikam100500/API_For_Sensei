from django.db import models


class Shop(models.Model):
    date = models.DateField()
    shop = models.CharField(max_length=60)
    country = models.CharField(max_length=2)
    visitors = models.IntegerField()
    earnings = models.IntegerField()
