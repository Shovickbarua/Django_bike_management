from django.db import models
from Category.models import Category

# Create your models here.
class Product(models.Model):
        product_name = models.CharField(max_length = 250)
        SKU         = models.CharField(max_length = 250)
        cat         = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
        dob         = models.DateField()
        quantity    = models.CharField(max_length = 250)
        cost        = models.CharField(max_length = 250)
        pro_image   = models.ImageField(null=True, blank=True, upload_to='images')