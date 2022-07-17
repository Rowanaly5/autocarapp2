
class InvoiceModel(models.Model):
    invoice_date               = models.DateField(default=now)
    payment_method             = models.CharField(max_length=50, default='', blank=True, null=True, choices=payments)
    invoice_foreign_id         = models.ForeignKey(JobModel, blank=True,  default=0 , null=True, on_delete=models.CASCADE)
    invoice_id                 = models.AutoField(primary_key=True)
    customer_name              = models.CharField(JobModel,max_length=100 , blank=True ,null=True)
    customer_address           = models.TextField(JobModel,blank=True , default='', null=True,  max_length=200)
    customer_email             = models.EmailField(JobModel,blank=True, default='' ,null=True)
    job_date                   = models.DateField(JobModel,default=now)
    service_one                = models.TextField('Service 1', max_length=120, default='', blank=True, null=True)
    service_one_price          = models.IntegerField('Unit Price', default=0, blank=True, null=True)
    service_two                = models.TextField('Service 2', max_length=120, default='', blank=True, null=True)
    service_two_price          = models.IntegerField('Unit Price ', default=0, blank=True, null=True)
    service_three              = models.TextField('Service 3', max_length=120, default='', blank=True, null=True)
    service_three_price        = models.IntegerField('Unit Price ', default=0, blank=True, null=True)
    service_four               = models.TextField('Service 4', max_length=120, default='', blank=True, null=True)
    service_four_price         = models.IntegerField('Unit Price ', default=0, blank=True, null=True)
    service_five               = models.TextField('Service 5', max_length=120, default='', blank=True, null=True)
    service_five_price         = models.IntegerField('Unit Price ', default=0, blank=True, null=True)
    service_six                = models.TextField('Service 6', max_length=120, default='', blank=True, null=True)
    service_six_price          = models.IntegerField('Unit Price ', default=0, blank=True, null=True)
    service_seven              = models.TextField('Service 7', max_length=120, default='', blank=True, null=True)
    service_seven_price        = models.IntegerField('Unit Price ', default=0, blank=True, null=True)
    service_eight              = models.TextField('Service 8', max_length=120, default='', blank=True, null=True)
    service_eight_price        = models.IntegerField('Unit Price ', default=0, blank=True, null=True)
    service_nine               = models.TextField('Service 9', max_length=120, default='', blank=True, null=True)
    service_nine_price         = models.IntegerField('Unit Price ', default=0, blank=True, null=True)
    service_ten                = models.TextField('Service 10', max_length=120, default='', blank=True, null=True)
    service_ten_price          = models.IntegerField('Unit Price ', default=0, blank=True, null=True)
    
    def _get_total(self):
        return service_one_price + service_two_price + service_three_price + service_four_price + service_five_price + service_six_price + service_seven_price + service_eight_price +service_nine_price +service_ten_price
    total = property(_get_total)

    def __unicode__(self):
        return self.invoice_id   







        <br><br>
        <div class="form-group col-md-6 ">
          <label for="">Sevice 3</label>
          <input type="text" class="form-control form-control-sm" style="margin-left:140px" name="service_three" value="{{values.service_three}}"/>
        </div>

        <div class="form-group col-md-6 ">
          <label for="">Price $ </label>
            <input type="price"  class="form-control form-control-sm" style="margin-left:165px"  name="service_three_price" value="{{values.service_three_price}}"/>
          </div>

          <br><br>
        <div class="form-group col-md-6 ">
          <label for="">Sevice 4</label>
          <input type="text" class="form-control form-control-sm" style="margin-left:140px" name="service_four" value="{{values.service_four}}"/>
        </div>

        <div class="form-group col-md-6 ">
          <label for="">Price $ </label>
            <input type="price"  class="form-control form-control-sm" style="margin-left:165px"  name="service_four_price" value="{{values.service_four_price}}"/>
          </div>

          <br><br>
        <div class="form-group col-md-6 ">
          <label for="">Sevice 5</label>
          <input type="text" class="form-control form-control-sm" style="margin-left:140px" name="service_five" value="{{values.service_five}}"/>
        </div>

        <div class="form-group col-md-6 ">
          <label for="">Price $ </label>
            <input type="price"  class="form-control form-control-sm" style="margin-left:165px"  name="service_five_price" value="{{values.service_five_price}}"/>
          </div>

          <br><br><br>

        <div class="form-group col-md-6 ">
          <label for="">Sevice 6</label>
          <input type="text" class="form-control form-control-sm" style="margin-left:140px" name="service_six" value="{{values.service_six}}"/>
        </div>

        <div class="form-group col-md-6 ">
          <label for="">Price $ </label>
            <input type="price"  class="form-control form-control-sm" style="margin-left:165px"  name="service_six_price" value="{{values.service_six_price}}"/>
          </div> 