from django.db import models

# Create your models here.


class Myself(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    about_me = models.TextField()
    photo = models.ImageField(blank=True)
    github = models.CharField(max_length=500, blank=True)
    linkedin = models.CharField(max_length=500, blank=True)
