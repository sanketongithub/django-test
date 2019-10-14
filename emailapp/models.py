from django.db import models

# Create your models here.
from django.db.models import DateTimeField



class Emailheader(models.Model):

    company_name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    address = models.TextField()


class Emailfooter(models.Model):

     company_name = models.CharField(max_length=200)  
     website_url = models.CharField(max_length=100) 
     contact_no = models.IntegerField()


class EmployeesTest(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length= 10)
    birth_date = models.DateTimeField(null=True, blank=True)
    hire_date = models.DateTimeField(null=True, blank=True)


class Employees(models.Model):
    emp_no = models.IntegerField()
    birth_date = models.DateTimeField(null=True, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    hire_date = models.DateTimeField(null=True, blank=True)










