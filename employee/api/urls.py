from django.urls import path
from .views import *

urlpatterns = [
    path('', EmployeeView),
    path('post', EmployeePost),

]