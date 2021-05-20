from django.db import models
# Create your models here.

class documents(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    result=models.CharField(max_length=50)
    
    