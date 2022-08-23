from rest_framework import serializers

from .models import *


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'age', 'gender', 'phoneNo', 'photo']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['hno', 'street', 'city', 'state']


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ['companyName', 'fromDate', 'toDate', 'address']


class QualificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualifications
        fields = ['qualificationName', 'fromDate', 'toDate', 'percentage']


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['title', 'description']

