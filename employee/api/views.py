from django.shortcuts import render, redirect
import base64
from django.core.files.base import ContentFile
from rest_framework import status

from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def EmployeeView(request):
    profiles = Employee.objects.all()
    emp = []
    for i in profiles:
        d = {}
        d['regid'] = i.regid
        d['name'] = i.name
        d['email'] = i.email
        d['age'] = i.age
        d['gender'] = i.gender
        d['phoneNo'] = i.phoneNo
        d['addressDetails'] = {}
        address = Address.objects.get(employee=i)
        d['addressDetails']['hno'] = address.hno
        d['addressDetails']['street'] = address.street
        d['addressDetails']['city'] = address.city
        d['addressDetails']['state'] = address.state
        d['workExperience'] = []
        for j in WorkExperience.objects.filter(employee=i):
            f = {}
            f['companyName'] = j.companyName
            f['fromDate'] = j.fromDate
            f['toDate'] = j.toDate
            f['address'] = j.address
            d['workExperience'].append(f)
        d['qualifications'] = []
        for j in Qualifications.objects.filter(employee=i):
            f = {}
            f['qualificationName'] = j.qualificationName
            f['fromDate'] = j.fromDate
            f['toDate'] = j.toDate
            f['percentage'] = j.percentage
            d['qualifications'].append(f)
        d['projects'] = []
        for j in Projects.objects.filter(employee=i):
            f = {}
            f['title'] = j.title
            f['description'] = j.description
            d['projects'].append(f)
        d['photo'] = str(i.photo)
        emp.append(d)
    return Response(emp)

@api_view(['POST'])
def EmployeePost(request):
    try:
        data = request.data
        create_works = []
        create_quali = []
        create_projects = []
        try:
            Employee.objects.get(email__iexact=data['email'])
            return Response({'message': 'employee already exist', 'success': False},
                            status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            e = {}
            e['name'] = data['name']
            e['email'] = data['email']
            e['age'] = data['age']
            e['gender'] = data['gender']
            e['phoneNo'] = data['phoneNo']
            e['photo'] = data['photo']
            employee = EmployeeSerializer(data=e)
            if employee.is_valid():
                pass
            else:
                return Response(employee.errors, status=status.HTTP_400_BAD_REQUEST)
            a = {}
            a['hno'] = data['addressDetails']['hno']
            a['street'] = data['addressDetails']['street']
            a['city'] = data['addressDetails']['city']
            a['state'] = data['addressDetails']['state']
            address = AddressSerializer(data=a)
            if address.is_valid():
                pass
            else:
                return Response(address.errors, status=status.HTTP_400_BAD_REQUEST)
            try:
                works = data['workExperience']
                for i in works:
                    w = {}
                    w['companyName'] = i['companyName']
                    w['fromDate'] = i['fromDate']
                    w['toDate'] = i['toDate']
                    w['address'] = i['address']

                    work = WorkExperienceSerializer(data=w)
                    if work.is_valid():
                        create_works.append(work)
                    else:
                        return Response(work.errors, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({'message': 'workExperience missing', 'success': False},
                                status=status.HTTP_400_BAD_REQUEST)
            try:
                qualifications = data['qualifications']
                for i in qualifications:
                    q = {}
                    q['qualificationName'] = i['qualificationName']
                    q['fromDate'] = i['fromDate']
                    q['toDate'] = i['toDate']
                    q['percentage'] = i['percentage']

                    quali = QualificationsSerializer(data=q)
                    if quali.is_valid():
                        create_quali.append(quali)
                    else:
                        return Response(quali.errors, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({'message': 'qualifications missing', 'success': False},
                                status=status.HTTP_400_BAD_REQUEST)
            try:
                projects = data['projects']
                for i in projects:
                    p = {}
                    p['title'] = i['title']
                    p['description'] = i['description']
                    project = ProjectsSerializer(data=p)
                    if project.is_valid():
                        create_projects.append(project)
                    else:
                        return Response(project.errors, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({'message': 'projects missing', 'success': False},
                                status=status.HTTP_400_BAD_REQUEST)

            e = employee.save()
            try:
                emp = empID.objects.get(id=1)
                emp.last += 1
                emp.save()
                emp_id = emp.last
            except empID.DoesNotExist:
                emp_id = 1
                empID.objects.create(last=emp_id)
            regid = 'EMP'+str(emp_id)
            e.regid = regid
            e.save()
            a = address.save()
            a.employee = e
            a.save()
            for i in create_works:
                w = i.save()
                w.employee = e
                w.save()
            for i in create_quali:
                q = i.save()
                q.employee = e
                q.save()
            for i in create_projects:
                p = i.save()
                p.employee = e
                p.save()
            return Response({'message': 'employee created successfully', 'regid': regid, 'success': True},
                            status=status.HTTP_200_OK)
    except:
        return Response({'message': 'employee created failed', 'success': False},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
