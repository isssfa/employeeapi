from django.urls import path
from .views import *

urlpatterns = [
    path('', EmployeeIndex),
    path('post', EmployeePost),
    path('get', EmployeeViewAll),
    path('get/', EmployeeViewAll),
    path('get/<str:regid>', EmployeeViewSingle),
    path('put/<str:regid>', EmployeePut),
    path('delete/<str:regid>', EmployeeDelete),
]