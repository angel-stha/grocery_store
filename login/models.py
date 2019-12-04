from django.db import models

# Create your models here.

class Items(models.Model):
    item_name = models.CharField(max_length=100)
    category =models.CharField(max_length=9)
    stock = models.IntegerField()
    selling_price = models.IntegerField()
# class Buyer(models.Model):
#  b_id=    