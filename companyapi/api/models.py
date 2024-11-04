from tkinter.constants import CASCADE

from django.db import models
from django.db.models import TextField


# Create your models here.

# Company model

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    location= models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    type = models.CharField(max_length=200,choices=(('IT','IT'),('Non IT','Non IT'),('Mobile phone','Mobile phone')))
    added_date= models.DateTimeField(auto_now=True)
    about = TextField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    about = models.TextField()
    phone= models.CharField(max_length=50)
    position = models.CharField(max_length=50,choices=(('Manager','manager'),('Software developer','sd'),('Tester','tt')))
    address = models.CharField(max_length=200)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)