from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    source = models.CharField(blank=True)
    site = models.CharField(blank=True)