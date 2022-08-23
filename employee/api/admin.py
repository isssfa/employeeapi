from django.contrib import admin
from .models import *


# Register your models here.
class EmpSearch(admin.ModelAdmin):
    search_fields = ['name', 'email']
    list_display = ['name', 'email', 'age', 'gender', 'phoneNo']


class AddSearch(admin.ModelAdmin):
    search_fields = ['employee__name', 'employee__email']
    list_display = ['employee', 'hno', 'street', 'city', 'state']


class WorkSearch(admin.ModelAdmin):
    search_fields = ['employee__name', 'employee__email']
    list_display = ['employee', 'companyName', 'fromDate', 'toDate']


class QualificationSearch(admin.ModelAdmin):
    search_fields = ['employee__name', 'employee__email']
    list_display = ['employee', 'qualificationName', 'percentage']


class ProjectSearch(admin.ModelAdmin):
    search_fields = ['employee__name', 'employee__email']
    list_display = ['employee', 'title']


admin.site.register(Employee, EmpSearch)
admin.site.register(Address, AddSearch)
admin.site.register(WorkExperience, WorkSearch)
admin.site.register(Qualifications, QualificationSearch)
admin.site.register(Projects, ProjectSearch)
admin.site.register(empID)
