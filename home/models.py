from django.db import models


# Create your models here.
class tile(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100)
    d=models.CharField(max_length=300)
    img=models.ImageField()
    def __str__(self):
        return self.product_name

class customer(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.product_name
    
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    issue=models.CharField( max_length=100)

    