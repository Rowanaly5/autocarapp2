

from django import views
from django import urls
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from common.views import SignUpView, ProfileUpdateView, ProfileView
from JobApp import views 
from common import views 
from django.contrib.auth import views as auth_views
from django.urls import include, re_path

urlpatterns = [
    path('jobs/',include('JobApp.urls')),
    path('',include('common.urls')),

    path('admin', admin.site.urls),
    

]