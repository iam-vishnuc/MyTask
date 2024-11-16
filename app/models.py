from django.db import models

# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)


class Gallery(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    