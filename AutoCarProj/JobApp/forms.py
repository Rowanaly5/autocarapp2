from django import forms
from JobApp.models import JobModel 

class JobForm(forms.ModelForm):
    class Meta:
        model = JobModel
        fields = ['customer_name', 'customer_phone' ,'customer_address',
                'customer_email' ,
                'car_model' , 'car_chassis' ,'car_number' , 'car_mileage',
                'car_color' , 'job_date' , 'job_comments','job_notes' , 
                'invoice_date' , 'payment_method' ,'service_one' ,
                'service_two' , 'total',

                
                ]
        
        
        
        
class JobSearchForm(forms.ModelForm):
    class Meta:
        model = JobModel
        fields = ['customer_name', 'customer_phone' , 'customer_email' ,'job_id']