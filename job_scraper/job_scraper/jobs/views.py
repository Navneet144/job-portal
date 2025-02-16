from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
import numpy as np
from pymongo import MongoClient
from bson.objectid import ObjectId  # Required for MongoDB object IDs
from .models import Job
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

# MongoDB Connection
client = MongoClient("mongodb+srv://nkumarnkumar900544:cAufg88hcRONhUCH@cluster0.oqox0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["job_scraper"]
collection = db["jobs"]

def average_salary_view(request):
    jobs = list(collection.find())
    salaries = [float(job["salary"]) for job in jobs if job.get("salary") and job["salary"].isdigit()]
    
    avg_salary = np.mean(salaries) if salaries else 0
    return JsonResponse({"average_salary": avg_salary})
def job_list(request):
    jobs = list(collection.find({}, {"id": 1, "title": 1, "company": 1, "location": 1, "salary": 1}))
    salaries = [float(job["salary"]) for job in jobs if "salary" in job and str(job["salary"]).isdigit()]
    avg_salary = np.mean(salaries) if salaries else "Not specified"
    return render(request, "jobs/job_list.html", {"jobs": jobs, "avg_salary": avg_salary})

def admin_check(user):
    return user.is_superuser

@login_required
@staff_member_required 
# Edit job (admin only)
def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == "POST":
        job.company = request.POST["company"]
        job.location = request.POST["location"]
        job.salary = request.POST["salary"]
        job.apply_link = request.POST["apply_link"]
        job.save()
        return redirect("/")  # Redirect to job listing
    return render(request, "jobs/edit_job.html", {"job": job})

@login_required
@staff_member_required
# Delete job (admin only)
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    job.delete()
    return redirect("/")  # Redirect to job listing

def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    

