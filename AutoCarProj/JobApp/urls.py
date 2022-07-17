from django.urls import path, include
from JobApp import views 

urlpatterns = [


    path('job-index', views.job_index, name="job-index"),
    path('job-index-arb', views.job_index_arb, name="job-index-arb"),
    
    path('job-search', views.job_search, name='job-search'),
    path('job-search-arb', views.job_search_arb, name='job-search-arb'),

    path('add-job', views.add_job, name="add-job"),
    path('add-job-arb', views.add_job_arb, name="add-job-arb"),

    path('edit-job/<int:id>', views.job_edit, name="job-edit"),
    path('edit-job-arb/<int:id>', views.job_edit_arb, name="job-edit-arb"),

    path('job-delete/<int:id>', views.delete_job, name="job-delete"),
    path('job-delete-arb/<int:id>', views.delete_job_arb, name="job-delete-arb"),

    path('job-detail/<int:id>/', views.job_detail ,name="job-detail" ),
    path('job-detail-arb/<int:id>/', views.job_detail_arb ,name="job-detail-arb" ),

    path('invoice-index', views.invoice_index, name="invoice-index"),
    path('invoice-index-arb', views.invoice_index_arb, name="invoice-index-arb"),

    path('invoice-detail/<int:id>/', views.invoice_detail ,name="invoice-detail" ),
    path('invoice-detail-arb/<int:id>/', views.invoice_detail_arb ,name="invoice-detail-arb" ),
    
    path('edit-invoice/<int:id>', views.invoice_edit, name="invoice-edit"),
    path('edit-invoice-arb/<int:id>', views.invoice_edit_arb, name="invoice-edit-arb"),

    path('invoice-search', views.invoice_search, name='invoice-search'),
    path('invoice-search-arb', views.invoice_search_arb, name='invoice-search-arb'),
    
    
    path('invoice-export-csv', views.invoice_export_csv ,name="invoice-export-csv" ),
    #path('job-export-csv', views.job_export_csv ,name="job-export-csv" ),

]