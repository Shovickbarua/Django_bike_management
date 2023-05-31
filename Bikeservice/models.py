from django.db import models

# Create your models here.


class Bikeservice(models.Model):

    invoiceId   = models.CharField(max_length=250)
    client_name = models.CharField(max_length=250)
    contact     = models.CharField(max_length=250)
    address     = models.CharField(max_length=250)
    bike_name   = models.CharField(max_length=250)
    service_type   = models.CharField(max_length=250)
    first_service         = models.DateField()
    second_service         = models.DateField()
    third_service         = models.DateField()
    fourth_service         = models.DateField()
    fifth_service         = models.DateField()
    sixth_service         = models.DateField()
    seventh_service         = models.DateField()
    eighth_service         = models.DateField()
   


# Create your models here.
