from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=100),
    password = models.CharField(max_length=8)
class Items(models.Model):
    item_name = models.CharField(max_length=100)
    category =models.CharField(max_length=9)
    stock = models.IntegerField()
    selling_price = models.IntegerField()
class Buyer(models.Model):
    b_id = models.IntegerField()
    b_name =models.CharField(max_length=100)
    b_contact=models.CharField(max_length=12)
    b_debit=models.IntegerField(100)

    def __str__(self):
        return self.b_name 