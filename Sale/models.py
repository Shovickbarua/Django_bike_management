from django.db import models
# Create your models here.
class Sale(models.Model):
        invoiceId       = models.CharField(max_length = 250)
        cat_name        = models.CharField(max_length = 250)
        product_name    = models.CharField(max_length = 250)
        pro_quantity    = models.CharField(max_length = 250)
        sale            = models.CharField(max_length = 250)
        cus_name        = models.CharField(max_length = 250)
        product_name    = models.CharField(max_length = 250)
        address         = models.CharField(max_length = 250)
        method          = models.CharField(max_length = 250)
        contact         = models.CharField(max_length = 250)
        dob             = models.DateField()
        cost            = models.CharField(max_length = 250)
        SKU             = models.CharField(max_length = 250)
        profit          = models.CharField(max_length = 250)
        total           = models.CharField(max_length = 250)
