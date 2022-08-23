from django.db import models


# Create your models here.
class Employee(models.Model):
    regid = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    phoneNo = models.CharField(max_length=20)
    photo = models.TextField()

    def __str__(self):
        return self.name


class Address(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, null=True, blank=True)
    hno = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)


class WorkExperience(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    companyName = models.CharField(max_length=200)
    fromDate = models.CharField(max_length=200)
    toDate = models.CharField(max_length=200)
    address = models.TextField()


class Qualifications(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    qualificationName = models.CharField(max_length=200)
    fromDate = models.CharField(max_length=200, null=True, blank=True)
    toDate = models.CharField(max_length=200, null=True, blank=True)
    percentage = models.FloatField()


class Projects(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()


class empID(models.Model):
    last = models.IntegerField()

    def __str__(self):
        return self.last