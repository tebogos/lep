from django.db import models

# Create your models here.

class Firm(models.Model):
    firm_no = models.CharField(max_length=6,unique=True )
    firm_name=models.CharField(max_length=255,unique=True)
    firm_contact=models.CharField(max_length=10)
    firm_email=models.EmailField(max_length=255)
    def __str__(self):
       return self.firm_name
    
