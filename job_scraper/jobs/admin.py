from django.contrib import admin
from .models import Job

# Unregister the Job model if already registered
try:
    admin.site.unregister(Job)
except admin.sites.NotRegistered:
    pass

class JobAdmin(admin.ModelAdmin):
    list_display = ("company", "location", "salary")  # Show in admin panel
    search_fields = ("company", "location")
      # Ensure salary_min exists in the model

    def average_salary(self, obj):
        if obj.salary_min and obj.salary_max:
            return f"₹{obj.salary_min} - ₹{obj.salary_max}"
        return "Not specified"
    
    average_salary.short_description = "Salary"

admin.site.register(Job, JobAdmin)  # Register it only once
