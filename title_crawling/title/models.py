from django.db import models

# Create your models here.
class SearchTitle(models.Model):
    words = models.CharField(max_length=50)