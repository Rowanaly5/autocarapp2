from urllib import response
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from JobApp.models import JobModel 
from django.db.models import F
from django.views.generic.edit import DeleteView
from django.db.models import Q

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
import datetime
# For Report Lab                                               
from django.db.models import Sum
from .forms import JobSearchForm  , JobForm
import json
from django.http import JsonResponse
# Create your views here.
from .forms import JobForm
from .forms import JobSearchForm
from django.http import HttpResponse
from django.conf import settings
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
import csv
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import csv



def invoice_export_csv(request):
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=jobs.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Customer Name', 'Customer Phone', 'Customer Address', 'Customer Email',
                'Car Model', 'Car Chassis' , 'Car Number' , 'Car Mileage' , 'Car Color' , 'Job Date' , 'Job Comment' ,
                'Job Notes' , "Invoice Date" , 'Payment Method' , 'Serice One' , 'Service One Price ' , 'Service Two ' , 'Service Two Price','Total'])
    studs = JobModel.objects.get()('job_id','customer_name', 'customer_phone' ,'customer_address','customer_email' ,
                'car_model' , 'car_chassis' ,'car_number' , 'car_mileage',
                'car_color' , 'job_date' , 'job_comments','job_notes' , 
                'invoice_date' , 'payment_method' ,'service_one' ,'service_one_price',
                'service_two' ,'service_two_price', 'total')
    for std in studs:
        writer.writerow(std)
    return response



def job_index(request):
    title = 'List of Jobs'
    queryset = JobModel.objects.all()
    form = JobSearchForm(request.POST or None)
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
		"title": title,
		"queryset": queryset,
        'page_obj': page_obj,
	}
    return render(request, 'jobs/job_index.html', context)

def job_index_arb(request):
    title = 'List of Jobs'
    queryset = JobModel.objects.all()
    form = JobSearchForm(request.POST or None)
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
		"title": title,
		"queryset": queryset,
        'page_obj': page_obj,
	}
    return render(request, 'jobs_arb/job_index_arb.html', context)


def add_job(request):
    jobs = JobModel.objects.all()
    form = JobForm(request.POST or None)

    context = {
        'jobs' : jobs,
        "form": form,
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'jobs/add_job.html', context)

    if request.method == 'POST':
        customer_name          =  request.POST.get('customer_name', False)
        customer_phone         =  request.POST.get('customer_phone', False)
        customer_address       =  request.POST.get('customer_address', False)
        customer_email         =  request.POST.get('customer_email', False)
        car_model              =  request.POST.get('car_model', False)
        car_chassis            =  request.POST.get('car_chassis', False)
        car_number             =  request.POST.get('car_number', False)
        car_mileage            =  request.POST.get('car_mileage', False)
        car_color              =  request.POST.get('car_color', False)
        job_date               =  request.POST.get('job_date', False)
        job_comments           =  request.POST.get('job_comments', False)
        job_notes              =  request.POST.get('job_notes', False)
        invoice_date           =  request.POST.get('invoice_date', False)
        payment_method         =  request.POST.get('payment_method', False)
        service_one            =  request.POST.get('service_one', False)
        service_one_price      =  request.POST.get('service_one_price', False)
        service_two            =  request.POST.get('service_two', False)
        service_two_price      =  request.POST.get('service_two_price', False)
        service_three          =  request.POST.get('service_three', False)
        service_three_price    =  request.POST.get('service_three_price', False)
        service_four           =  request.POST.get('service_four', False)
        service_four_price     =  request.POST.get('service_four_price', False)
        service_five           =  request.POST.get('service_five', False)
        service_five_price     =  request.POST.get('service_five_price', False)
        service_six            =  request.POST.get('service_six', False)
        service_six_price      =  request.POST.get('service_six_price', False)
        service_seven          =  request.POST.get('service_seven', False)
        service_seven_price    =  request.POST.get('service_seven_price', False)
        service_eight          =  request.POST.get('service_eight', False)
        service_eight_price    =  request.POST.get('service_eight_price', False)
        service_nine           =  request.POST.get('service_nine', False)
        service_nine_price     =  request.POST.get('service_nine_price', False)
        service_ten            =  request.POST.get('service_ten', False)
        service_ten_price      =  request.POST.get('service_ten_price', False)
        total                  =  request.POST.get('total', False)

    
        if not customer_name:
            messages.warning(request, 'Customer Name is required')
            return render(request, 'jobs/add_job.html', context)
        if not customer_phone:
            messages.warning(request, 'Customer Phone is required')
            return render(request, 'jobs/add_job.html', context)
        if not customer_address:
            messages.warning(request, 'Customer Address is required')
            return render(request, 'jobs/add_job.html', context)
        if not customer_email:
            messages.warning(request, 'Customer Email is required')
            return render(request, 'jobs/add_job.html', context)
        if not car_model:
            messages.warning(request, 'Car Model is required')
            return render(request, 'jobs/add_job.html', context)
        if not car_chassis:
            messages.warning(request, 'Car Chassis is required')
            return render(request, 'jobs/add_job.html', context)
        if not car_number:
            messages.warning(request, 'Car Number is required')
            return render(request, 'jobs/add_job.html', context)
        if not car_color:
            messages.warning(request, 'Car Color is required')
            return render(request, 'jobs/add_job.html', context)
        if not car_mileage:
            messages.warning(request, 'Car Mileage is required')
            return render(request, 'jobs/add_job.html', context)
        if not job_date:
            messages.warning(request, 'Car Date is required')
            return render(request, 'jobs/add_job.html', context)
    
        JobModel.objects.create(
                            customer_name=customer_name , customer_phone=customer_phone,
                            customer_address=customer_address, customer_email=customer_email ,
                            car_model =car_model, car_chassis=car_chassis ,car_number=car_number ,
                            car_mileage=car_mileage ,car_color=car_color, 
                            job_date=job_date ,job_comments=job_comments ,
                            job_notes=job_notes ,
                            invoice_date=invoice_date, payment_method=payment_method,
                            service_one   = service_one   , service_one_price      = service_one_price ,
                            service_two   = service_two   , service_two_price      = service_two_price ,
                            service_three = service_three , service_three_price    = service_three_price ,
                            service_four  = service_four  , service_four_price     = service_four_price ,
                            service_five  = service_five  , service_five_price     = service_five_price ,
                            service_six   = service_six   ,  service_six_price     = service_six_price ,
                            service_seven = service_seven , service_seven_price    = service_seven_price ,
                            service_eight = service_eight , service_eight_price    = service_eight_price ,
                            service_nine  = service_nine  , service_nine_price     = service_nine_price ,
                            service_ten   = service_ten   , service_ten_price      = service_ten_price , total=total
                            )
        
        messages.success(request, 'Changes saved successfully')

        return redirect('job-index')
    

def add_job_arb(request):
    jobs = JobModel.objects.all()
    form = JobForm(request.POST or None)

    context = {
        'jobs' : jobs,
        "form": form,
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'jobs_arb/add_job_arb.html', context)

    if request.method == 'POST':
        customer_name          =  request.POST.get('customer_name', False)
        customer_phone         =  request.POST.get('customer_phone', False)
        customer_address       =  request.POST.get('customer_address', False)
        customer_email         =  request.POST.get('customer_email', False)
        car_model              =  request.POST.get('car_model', False)
        car_chassis            =  request.POST.get('car_chassis', False)
        car_number             =  request.POST.get('car_number', False)
        car_mileage            =  request.POST.get('car_mileage', False)
        car_color              =  request.POST.get('car_color', False)
        job_date               =  request.POST.get('job_date', False)
        job_comments           =  request.POST.get('job_comments', False)
        job_notes              =  request.POST.get('job_notes', False)
        invoice_date           =  request.POST.get('invoice_date', False)
        payment_method         =  request.POST.get('payment_method', False)
        service_one            =  request.POST.get('service_one', False)
        service_one_price      =  request.POST.get('service_one_price', False)
        service_two            =  request.POST.get('service_two', False)
        service_two_price      =  request.POST.get('service_two_price', False)
        service_three          =  request.POST.get('service_three', False)
        service_three_price    =  request.POST.get('service_three_price', False)
        service_four           =  request.POST.get('service_four', False)
        service_four_price     =  request.POST.get('service_four_price', False)
        service_five           =  request.POST.get('service_five', False)
        service_five_price     =  request.POST.get('service_five_price', False)
        service_six            =  request.POST.get('service_six', False)
        service_six_price      =  request.POST.get('service_six_price', False)
        service_seven          =  request.POST.get('service_seven', False)
        service_seven_price    =  request.POST.get('service_seven_price', False)
        service_eight          =  request.POST.get('service_eight', False)
        service_eight_price    =  request.POST.get('service_eight_price', False)
        service_nine           =  request.POST.get('service_nine', False)
        service_nine_price     =  request.POST.get('service_nine_price', False)
        service_ten            =  request.POST.get('service_ten', False)
        service_ten_price      =  request.POST.get('service_ten_price', False)
        total                  =  request.POST.get('total', False)

    
        if not customer_name:
            messages.warning(request, 'Customer Name is required')
            return render(request, 'jobs_arb/add_job_arb.html', context)
        if not customer_phone:
            messages.warning(request, 'Customer Phone is required')
            return render(request, 'jobs_arb/add_job_arb.html', context)
        if not customer_address:
            messages.warning(request, 'Customer Address is required')
            return render(request, 'jobs_arb/add_job_arb.html', context)
        if not customer_email:
            messages.warning(request, 'Customer Email is required')
            return render(request, 'jobs_arb/add_job_arb.html', context)
        if not car_model:
            messages.warning(request, 'Car Model is required')
            return render(request, 'jobs_arb/add_job_arb.html', context)
        if not car_chassis:
            messages.warning(request, 'Car Chassis is required')
            return render(request, 'jobs_arb/add_job_arb.html', context)
        if not car_number:
            messages.warning(request, 'Car Number is required')
            return render(request, 'jobs_arb/add_job_arb.html', context)
        if not car_color:
            messages.warning(request, 'Car Color is required')
            return render(request, 'jobs_arb/add_job_arb.html', context)
        if not car_mileage:
            messages.warning(request, 'Car Mileage is required')
            return render(request, 'jobs_arb/add_job_arb.html', context)
        if not job_date:
            messages.warning(request, 'Car Date is required')
            return render(request, 'jobs_arb/add_job_arb.html', context)
    
        JobModel.objects.create(
                            customer_name=customer_name , customer_phone=customer_phone,
                            customer_address=customer_address, customer_email=customer_email ,
                            car_model =car_model, car_chassis=car_chassis ,car_number=car_number ,
                            car_mileage=car_mileage ,car_color=car_color, 
                            job_date=job_date ,job_comments=job_comments ,
                            job_notes=job_notes ,
                            invoice_date=invoice_date, payment_method=payment_method,
                            service_one   = service_one   , service_one_price      = service_one_price ,
                            service_two   = service_two   , service_two_price      = service_two_price ,
                            service_three = service_three , service_three_price    = service_three_price ,
                            service_four  = service_four  , service_four_price     = service_four_price ,
                            service_five  = service_five  , service_five_price     = service_five_price ,
                            service_six   = service_six   ,  service_six_price     = service_six_price ,
                            service_seven = service_seven , service_seven_price    = service_seven_price ,
                            service_eight = service_eight , service_eight_price    = service_eight_price ,
                            service_nine  = service_nine  , service_nine_price     = service_nine_price ,
                            service_ten   = service_ten   , service_ten_price      = service_ten_price , total=total
                            )
        
        messages.success(request, 'تم الحفط')

        return redirect('job-index-arb')    

def job_detail(request, id):
    job = JobModel.objects.get(job_id=id) # we insert this line to get the Band with that id
    return render(request,
    'jobs/job_detail.html',
    {'job': job}) # we update this line to pass the band to the template

def job_detail_arb(request, id):
    job = JobModel.objects.get(job_id=id) # we insert this line to get the Band with that id
    return render(request,
    'jobs_arb/job_detail_arb.html',
    {'job': job}) # we update this line to pass the band to the template

def job_edit(request, id):
    job = JobModel.objects.get(pk=id)
    context = {
        'job': job,
        'values': job,
    }
    if request.method == 'GET':
        return render(request, 'jobs/edit-job.html', context)
    if request.method == 'POST':
        customer_name         = request.POST['customer_name']
        customer_phone        =  request.POST['customer_phone']
        customer_address      =  request.POST['customer_address']
        customer_email        =  request.POST['customer_email']
        car_model             =  request.POST['car_model']
        car_chassis           =  request.POST['car_chassis']
        car_number            =  request.POST['car_number']
        car_mileage           =  request.POST['car_mileage']
        car_color             =  request.POST['car_color']
        job_comments          =  request.POST['job_comments']
        job_notes             =  request.POST['job_notes']


        if not customer_name:
            messages.warning(request, 'Customer Name is required')
            return render(request, 'jobs/edit-job.html', context)
        if not customer_phone:
            messages.warning(request, 'Customer Phone is required')
            return render(request, 'jobs/edit-job.html', context)
        if not customer_address:
            messages.warning(request, 'Customer Address is required')
            return render(request, 'jobs/edit-job.html', context)
        if not customer_email:
            messages.warning(request, 'Customer Email is required')
            return render(request,'jobs/edit-job.html', context)
        if not car_model:
            messages.warning(request, 'Car Model is required')
            return render(request,'jobs/edit-job.html', context)
        if not car_chassis:
            messages.warning(request, 'Car Chassis is required')
            return render(request, 'jobs/edit-job.html', context)
        if not car_number:
            messages.warning(request, 'Car Number is required')
            return render(request, 'jobs/edit-job.html', context)
        if not car_color:
            messages.warning(request, 'Car Color is required')
            return render(request, 'jobs/edit-job.html', context)
        if not car_mileage:
            messages.warning(request, 'Car Mileage is required')
            return render(request,  'jobs/edit-job.html', context)
    
        
        job.customer_name = customer_name
        job.customer_phone = customer_phone
        job.customer_address = customer_address
        job.customer_email = customer_email
        job.car_model = car_model
        job.car_chassis = car_chassis
        job.car_number = car_number
        job.car_color = car_color
        job.car_mileage = car_mileage
        job.job_comments = job_comments
        job.job_notes = job_notes


        job.save()
        messages.success(request, 'Job updated  successfully')

        return redirect('job-index')


def job_edit_arb(request, id):
    job = JobModel.objects.get(pk=id)
    context = {
        'job': job,
        'values': job,
    }
    if request.method == 'GET':
        return render(request, 'jobs_arb/edit-job-arb.html', context)
    if request.method == 'POST':
        customer_name         = request.POST['customer_name']
        customer_phone        =  request.POST['customer_phone']
        customer_address      =  request.POST['customer_address']
        customer_email        =  request.POST['customer_email']
        car_model             =  request.POST['car_model']
        car_chassis           =  request.POST['car_chassis']
        car_number            =  request.POST['car_number']
        car_mileage           =  request.POST['car_mileage']
        car_color             =  request.POST['car_color']
        job_comments          =  request.POST['job_comments']
        job_notes             =  request.POST['job_notes']


        if not customer_name:
            messages.warning(request, 'Customer Name is required')
            return render(request, 'jobs_arb/edit-job-arb.html', context)
        if not customer_phone:
            messages.warning(request, 'Customer Phone is required')
            return render(request, 'jobs_arb/edit-job-arb.html', context)
        if not customer_address:
            messages.warning(request, 'Customer Address is required')
            return render(request, 'jobs_arb/edit-job-arb.html', context)
        if not customer_email:
            messages.warning(request, 'Customer Email is required')
            return render(request, 'jobs_arb/edit-job-arb.html', context)
        if not car_model:
            messages.warning(request, 'Car Model is required')
            return render(request, 'jobs_arb/edit-job-arb.html', context)
        if not car_chassis:
            messages.warning(request, 'Car Chassis is required')
            return render(request, 'jobs_arb/edit-job-arb.html', context)
        if not car_number:
            messages.warning(request, 'Car Number is required')
            return render(request, 'jobs_arb/edit-job-arb.html', context)
        if not car_color:
            messages.warning(request, 'Car Color is required')
            return render(request, 'jobs_arb/edit-job-arb.html', context)
        if not car_mileage:
            messages.warning(request, 'Car Mileage is required')
            return render(request, 'jobs_arb/edit-job-arb.html', context)
    
        
        job.customer_name = customer_name
        job.customer_phone = customer_phone
        job.customer_address = customer_address
        job.customer_email = customer_email
        job.car_model = car_model
        job.car_chassis = car_chassis
        job.car_number = car_number
        job.car_color = car_color
        job.car_mileage = car_mileage
        job.job_comments = job_comments
        job.job_notes = job_notes


        job.save()
        messages.success(request, 'تم الحفط')

        return redirect('job-index-arb')

def delete_job(request, id):
    job = JobModel.objects.get(pk=id)
    job.delete()
    messages.success(request, 'Job Deleted')
    return redirect('job-index')

def delete_job_arb(request, id):
    job = JobModel.objects.get(pk=id)
    job.delete()
    messages.success(request, 'تم الحذف')
    return redirect('job-index-arb')


def job_search(request):

    results = []

    if request.method == "GET":

        query = request.GET.get('search')

        if query == '':

            query = 'None'

        results = JobModel.objects.filter(Q(customer_name__icontains=query) | Q(customer_phone__icontains=query)  )

    return render(request, 'jobs/job_search.html', {'query': query, 'results': results})

def job_search_arb(request):
    
    results = []

    if request.method == "GET":

        query = request.GET.get('search')

        if query == '':

            query = 'None'

        results = JobModel.objects.filter(Q(customer_name__icontains=query) | Q(customer_phone__icontains=query)  )

    return render(request, 'jobs_arb/job_search_arb.html', {'query': query, 'results': results})



def invoice_index(request):
    title = 'List of Invoices'
    queryset = JobModel.objects.all()
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
		"title": title,
		"queryset": queryset,
        'page_obj': page_obj,
	}        
    return render(request,  'jobs/index_invoice.html', context)


def invoice_index_arb(request):
    title = 'List of Invoices'
    queryset = JobModel.objects.all()
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
		"title": title,
		"queryset": queryset,
        'page_obj': page_obj,
	}        
    return render(request, 'jobs_arb/index_invoice_arb.html', context)

def invoice_detail(request, id):
    job = JobModel.objects.get(job_id=id) # we insert this line to get the Band with that id
    return render(request,
    'jobs/invoice_detail.html',
    {'job': job}) # we update this line to pass the band to the template
    
    
def invoice_detail_arb(request, id):
    job = JobModel.objects.get(job_id=id) # we insert this line to get the Band with that id
    return render(request,
    'jobs_arb/invoice_detail_arb.html',
    {'job': job}) # we update this line to pass the band to the template
    


def invoice_edit(request, id):
    job = JobModel.objects.get(pk=id)
    context = {
        'job': job,
        'values': job,
    }
    if request.method == 'GET':
        return render(request, 'jobs/edit-invoice.html', context)
    if request.method == 'POST':
        customer_name         = request.POST['customer_name']
        customer_phone        =  request.POST['customer_phone']
        customer_address      =  request.POST['customer_address']
        customer_email        =  request.POST['customer_email']
        car_model             =  request.POST['car_model']
        car_chassis           =  request.POST['car_chassis']
        car_number            =  request.POST['car_number']
        car_mileage           =  request.POST['car_mileage']
        car_color             =  request.POST['car_color']
        job_comments          =  request.POST['job_comments']
        job_notes             =  request.POST['job_notes']
        payment_method         =  request.POST.get('payment_method', False)
        service_one            =  request.POST.get('service_one', False)
        service_one_price      =  request.POST.get('service_one_price', False)
        service_two            =  request.POST.get('service_two', False)
        service_two_price      =  request.POST.get('service_two_price', False)
        service_three          =  request.POST.get('service_three', False)
        service_three_price    =  request.POST.get('service_three_price', False)
        service_four           =  request.POST.get('service_four', False)
        service_four_price     =  request.POST.get('service_four_price', False)
        service_five           =  request.POST.get('service_five', False)
        service_five_price     =  request.POST.get('service_five_price', False)
        service_six            =  request.POST.get('service_six', False)
        service_six_price      =  request.POST.get('service_six_price', False)
        service_seven          =  request.POST.get('service_seven', False)
        service_seven_price    =  request.POST.get('service_seven_price', False)
        service_eight          =  request.POST.get('service_eight', False)
        service_eight_price    =  request.POST.get('service_eight_price', False)
        service_nine           =  request.POST.get('service_nine', False)
        service_nine_price     =  request.POST.get('service_nine_price', False)
        service_ten            =  request.POST.get('service_ten', False)
        service_ten_price      =  request.POST.get('service_ten_price', False)


        if not customer_name:
            messages.warning(request, 'Customer Name is required')
            return render(request, 'jobs/edit-invoice.html', context)
        if not customer_phone:
            messages.warning(request, 'Customer Phone is required')
            return render(request, 'jobs/edit-invoice.html', context)
        if not customer_address:
            messages.warning(request, 'Customer Address is required')
            return render(request, 'jobs/edit-invoice.html', context)
        if not customer_email:
            messages.warning(request, 'Customer Email is required')
            return render(request,'jobs/edit-invoice.html', context)
        if not car_model:
            messages.warning(request, 'Car Model is required')
            return render(request,'jobs/edit-invoice.html', context)
        if not car_chassis:
            messages.warning(request, 'Car Chassis is required')
            return render(request, 'jobs/edit-invoice.html', context)
        if not car_number:
            messages.warning(request, 'Car Number is required')
            return render(request, 'jobs/edit-invoice.html', context)
        if not car_color:
            messages.warning(request, 'Car Color is required')
            return render(request, 'jobs/edit-invoice.html', context)
        if not car_mileage:
            messages.warning(request, 'Car Mileage is required')
            return render(request,  'jobs/edit-invoice.html', context)
    
        
        job.customer_name = customer_name
        job.customer_phone = customer_phone
        job.customer_address = customer_address
        job.customer_email = customer_email
        job.car_model = car_model
        job.car_chassis = car_chassis
        job.car_number = car_number
        job.car_color = car_color
        job.car_mileage = car_mileage
        job.job_comments = job_comments
        job.job_notes = job_notes
        job.payment_method = payment_method
        job.service_one = service_one
        job.service_one_price = service_one_price
        job.service_two = service_two
        job.service_two_price = service_two_price
        job.service_three = service_three
        job.service_three_price = service_three_price
        job.service_four = service_four
        job.service_four_price = service_four_price
        job.service_five = service_five
        job.service_five_price = service_five_price
        job.service_six = service_six
        job.service_six_price = service_six_price
        job.service_seven = service_seven
        job.service_seven_price = service_seven_price
        job.service_eight = service_eight
        job.service_eight_price = service_eight_price
        job.service_nine = service_nine
        job.service_nine_price = service_nine_price
        job.service_ten = service_ten
        job.service_ten_price = service_ten_price


        job.save()
        messages.success(request, 'Invoice updated  successfully')

        return redirect('invoice-index')



def invoice_edit_arb(request, id):
    job = JobModel.objects.get(pk=id)
    context = {
        'job': job,
        'values': job,
    }
    if request.method == 'GET':
        return render(request, 'jobs_arb/edit-invoice-arb.html', context)
    if request.method == 'POST':
        customer_name         = request.POST['customer_name']
        customer_phone        =  request.POST['customer_phone']
        customer_address      =  request.POST['customer_address']
        customer_email        =  request.POST['customer_email']
        car_model             =  request.POST['car_model']
        car_chassis           =  request.POST['car_chassis']
        car_number            =  request.POST['car_number']
        car_mileage           =  request.POST['car_mileage']
        car_color             =  request.POST['car_color']
        job_comments          =  request.POST['job_comments']
        job_notes             =  request.POST['job_notes']
        payment_method         =  request.POST.get('payment_method', False)
        service_one            =  request.POST.get('service_one', False)
        service_one_price      =  request.POST.get('service_one_price', False)
        service_two            =  request.POST.get('service_two', False)
        service_two_price      =  request.POST.get('service_two_price', False)
        service_three          =  request.POST.get('service_three', False)
        service_three_price    =  request.POST.get('service_three_price', False)
        service_four           =  request.POST.get('service_four', False)
        service_four_price     =  request.POST.get('service_four_price', False)
        service_five           =  request.POST.get('service_five', False)
        service_five_price     =  request.POST.get('service_five_price', False)
        service_six            =  request.POST.get('service_six', False)
        service_six_price      =  request.POST.get('service_six_price', False)
        service_seven          =  request.POST.get('service_seven', False)
        service_seven_price    =  request.POST.get('service_seven_price', False)
        service_eight          =  request.POST.get('service_eight', False)
        service_eight_price    =  request.POST.get('service_eight_price', False)
        service_nine           =  request.POST.get('service_nine', False)
        service_nine_price     =  request.POST.get('service_nine_price', False)
        service_ten            =  request.POST.get('service_ten', False)
        service_ten_price      =  request.POST.get('service_ten_price', False)


        if not customer_name:
            messages.warning(request, 'Customer Name is required')
            return render(request, 'jobs_arb/edit-invoice-arb.html', context)
        if not customer_phone:
            messages.warning(request, 'Customer Phone is required')
            return render(request, 'jobs_arb/edit-invoice-arb.html', context)
        if not customer_address:
            messages.warning(request, 'Customer Address is required')
            return render(request, 'jobs_arb/edit-invoice-arb.html', context)
        if not customer_email:
            messages.warning(request, 'Customer Email is required')
            return render(request, 'jobs_arb/edit-invoice-arb.html', context)
        if not car_model:
            messages.warning(request, 'Car Model is required')
            return render(request, 'jobs_arb/edit-invoice-arb.html', context)
        if not car_chassis:
            messages.warning(request, 'Car Chassis is required')
            return render(request, 'jobs_arb/edit-invoice-arb.html', context)
        if not car_number:
            messages.warning(request, 'Car Number is required')
            return render(request, 'jobs_arb/edit-invoice-arb.html', context)
        if not car_color:
            messages.warning(request, 'Car Color is required')
            return render(request, 'jobs_arb/edit-invoice-arb.html', context)
        if not car_mileage:
            messages.warning(request, 'Car Mileage is required')
            return render(request, 'jobs_arb/edit-invoice-arb.html', context)
    
        
        job.customer_name        = customer_name
        job.customer_phone       = customer_phone
        job.customer_address     = customer_address
        job.customer_email       = customer_email
        job.car_model            = car_model
        job.car_chassis          = car_chassis
        job.car_number           = car_number
        job.car_color            = car_color
        job.car_mileage          = car_mileage
        job.job_comments         = job_comments
        job.job_notes            = job_notes
        job.payment_method       = payment_method
        job.service_one          = service_one
        job.service_one_price    = service_one_price
        job.service_two          = service_two
        job.service_two_price    = service_two_price
        job.service_three        = service_three
        job.service_three_price  = service_three_price
        job.service_four         = service_four
        job.service_four_price   = service_four_price
        job.service_five         = service_five
        job.service_five_price   = service_five_price
        job.service_six          = service_six
        job.service_six_price    = service_six_price
        job.service_seven        = service_seven
        job.service_seven_price  = service_seven_price
        job.service_eight        = service_eight
        job.service_eight_price  = service_eight_price
        job.service_nine         = service_nine
        job.service_nine_price   = service_nine_price
        job.service_ten          = service_ten
        job.service_ten_price    = service_ten_price


        job.save()
        messages.success(request, 'تم الحفط')

        return redirect('invoice-index-arb')



def invoice_search(request):

    results = []

    if request.method == "GET":

        query = request.GET.get('search')

        if query == '':

            query = 'None'

        results = JobModel.objects.filter(Q(customer_name__icontains=query) | Q(customer_phone__icontains=query) | Q(job_id__icontains=query) )

    return render(request, 'jobs/invoice_search.html', {'query': query, 'results': results})

def invoice_search_arb(request):
    
    results = []

    if request.method == "GET":

        query = request.GET.get('search')

        if query == '':

            query = 'None'

        results = JobModel.objects.filter(Q(customer_name__icontains=query) | Q(customer_phone__icontains=query) | Q(job_id__icontains=query) )

    return render(request, 'jobs_arb/invoice_search_arb.html', {'query': query, 'results': results})

