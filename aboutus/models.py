from django.db import models

# Create your models here.
class Project(models.Model):
    Name = models.CharField(max_length= 100)
    Number = models.CharField(max_length= 250)
    Email = models.EmailField()