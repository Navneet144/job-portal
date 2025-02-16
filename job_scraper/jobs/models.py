from django.db import models
from django.contrib import admin
import numpy as np
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

class Job(models.Model):
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=255, null=True, blank=True)
    apply_link = models.URLField(max_length=500, null=True, blank=True)
    
    def average_salary(self):
        if self.salary_min and self.salary_max:
            return (self.salary_min + self.salary_max) / 2
        return "Not specified"

    def __str__(self):
        return self.company


    @classmethod
    def average_salary(cls, city):
        salaries = list(cls.objects.filter(location__icontains=city, title__icontains='Python Developer').values_list('salary', flat=True))
        return np.mean(salaries) if salaries else 0

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'salary')
    search_fields = ('title', 'company', 'location')
    list_filter = ('location',)
    ordering = ('-salary',)
