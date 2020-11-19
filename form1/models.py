from django.db import models

# Create your models here.

class FormData(models.Model):
    location1 = models.CharField(max_length=200)
    location2 = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    date = models.DateField(auto_now=False)
    time = models.TimeField(auto_now=False)
    severity = models.CharField(max_length=200)
    cause = models.CharField(max_length=200)
    actions = models.CharField(max_length=200)
    type_env = models.CharField(max_length=200,default= 'f', null=True ,blank=True )
    type_inju = models.CharField(max_length=200,default= 'f', null=True ,blank=True )
    type_property = models.CharField(max_length=200,default= 'f', null=True ,blank=True )
    type_vehicle = models.CharField(max_length=200,default= 'f', null=True ,blank=True )