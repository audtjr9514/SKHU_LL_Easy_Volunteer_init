from django.db import models
from django.contrib.auth.models import AbstractUser

class GeneralUser(AbstractUser):
    codeNum = models.IntegerField()
    phoneNum = models.IntegerField()
    job = models.ForeignKey('Job', on_delete=models.CASCADE)

    def __str(self):
        return self.first_name

class Job(models.Model):
    job = models.CharField(max_length=20)
    def __str__(self):
        return self.Name


class Product(models.Model):
    Namn = models.CharField(max_length=30)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    point = models.IntegerField()
    def __str__(self):
        return self.Name

class Brand(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', blank=True)
    def __str__(self):
        return self.Name

# Create your models here.
