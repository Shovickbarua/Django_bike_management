from django.db import models

# Create your models here.


class bikesale(models.Model):

    invoiceId   = models.CharField(max_length=250)
    client_name = models.CharField(max_length=250)
    fname       = models.CharField(max_length=250)
    nid         = models.CharField(max_length=250)
    method      = models.CharField(max_length=250)
    dob         = models.DateField()
    contact     = models.CharField(max_length=250)
    address     = models.CharField(max_length=250)
    brand       = models.CharField(max_length=250)
    bike_name   = models.CharField(max_length=250)
    bsquantity  = models.CharField(max_length=250)
    bcost       = models.CharField(max_length=250)
    color       = models.CharField(max_length=250)
    engine_no   = models.CharField(max_length=250)
    chas_no     = models.CharField(max_length=250)
    m_veh       = models.CharField(max_length=250)
    manu        = models.CharField(max_length=250)
    cc          = models.CharField(max_length=250)
    seat_cap    = models.CharField(max_length=250)
    brake       = models.CharField(max_length=250)
    ftyre       = models.CharField(max_length=250)
    rtyre       = models.CharField(max_length=250)
    weight      = models.CharField(max_length=250)
    sale_price  = models.CharField(max_length=250)
    registration = models.CharField(max_length=250)
    bank_draft  = models.CharField(max_length=250)
    brta        = models.CharField(max_length=250)
    profit      = models.CharField(max_length=250)
    total       = models.CharField(max_length=250)
    cus_photo   = models.ImageField(null=True, blank=True, upload_to='images')
    b_copy      = models.ImageField(null=True, blank=True, upload_to='images')
    r_slip      = models.ImageField(null=True, blank=True, upload_to='images')
    t_token     = models.ImageField(null=True, blank=True, upload_to='images')


 
        
    
