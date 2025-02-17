"""job_scraper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path
from jobs import views


urlpatterns = [
    path('admin/', admin.site.urls),
     path('', views.job_list, name='job_list'),
    path('average_salary/', views.average_salary_view, name='average_salary'),
    path('delete/<str:job_id>/', views.delete_job, name='delete_job'),
    path('edit/<str:job_id>/', views.edit_job, name='edit_job'),
]
