from django.db import models

# Create your models here.
class Expense(models.Model):
        name = models.CharField(max_length = 250)
        dob  = models.DateField()
        amount= models.CharField(max_length = 250)