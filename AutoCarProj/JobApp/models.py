from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from decimal import Decimal
from django.db.models import F, Sum
# Create your models here.
class JobModel(models.Model):
    job_id                     = models.AutoField(primary_key=True)
    customer_name              = models.CharField(max_length=200 , blank=True ,null=True)
    customer_phone             = models.TextField(blank=True , null=True,  max_length=200)
    customer_address           = models.TextField(blank=True , null=True,  max_length=200)
    customer_email             = models.EmailField(blank=True ,null=True)
    car_model                  = models.IntegerField(blank=True, null=True)
    car_chassis                = models.TextField(blank=True , null=True,  max_length=20)
    car_number                 = models.TextField(blank=True , null=True, max_length=20)
    car_mileage                = models.BigIntegerField( blank=True, null=True)
    car_color                  = models.TextField(max_length=50, blank=True, null=True)
    job_date                   = models.DateField(default=now)
    job_comments               = models.TextField(max_length=600, blank=True, null=True)
    job_notes                  = models.TextField(max_length=600,  blank=True, null=True)
    invoice_date               = models.DateField(default=now)
    service_one                = models.TextField('Service 1', max_length=120, default='', blank=True, null=True)
    service_one_price          =  models.BigIntegerField( blank=True, null=True, default=0)
    service_two                = models.TextField('Service 2',  default='', blank=True, null=True)
    service_two_price          =   models.BigIntegerField( blank=True, null=True, default=0)
    service_three              = models.TextField('Service 3', max_length=120, default='', blank=True, null=True)
    service_three_price        =   models.BigIntegerField( blank=True, null=True, default=0)
    service_four               = models.TextField('Service 4', max_length=120, default='', blank=True, null=True)
    service_four_price         =  models.BigIntegerField( blank=True, null=True , default=0)
    service_five               = models.TextField('Service 5', max_length=120, default='', blank=True, null=True)
    service_five_price         =  models.BigIntegerField( blank=True, null=True, default=0)
    service_six                = models.TextField('Service 6', max_length=120, default='', blank=True, null=True)
    service_six_price          =  models.BigIntegerField( blank=True, null=True, default=0)
    service_seven              = models.TextField('Service 7', max_length=120, default='', blank=True, null=True)
    service_seven_price        =   models.BigIntegerField( blank=True, null=True, default=0)
    service_eight              = models.TextField('Service 8', max_length=120, default='', blank=True, null=True)
    service_eight_price        =   models.BigIntegerField( blank=True, null=True, default=0)
    service_nine               = models.TextField('Service 9', max_length=120, default='', blank=True, null=True)
    service_nine_price         =   models.BigIntegerField( blank=True, null=True, default=0)
    service_ten                = models.TextField('Service 10', max_length=120, default='', blank=True, null=True)
    service_ten_price          =   models.BigIntegerField( blank=True, null=True, default=0)
    total                      = models.BigIntegerField( blank=True, null=True, default=0)

    payment_method_choice = (
			('Cash', 'Cash'),
			('Visa ', 'Visa '),
		)
    payment_method = models.CharField(max_length=50, default='', blank=True, null=True, choices=payment_method_choice)

    def __str__(self):
        return self.job_id
    
    
