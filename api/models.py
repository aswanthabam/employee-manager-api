from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.conf import settings
# Create your models here.
class CustomUser(AbstractUser):
  USERNAME_FIELD = "username"
  first_name = models.CharField(max_length=200,null=False,blank=False)
  last_name = models.CharField(max_length=100,null=False,blank=False)
  email = models.EmailField(unique=True,null=False,blank=False)
  REQUIRED_FIELDS = ('first_name','last_name','email','password',) 

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True,unique=True)
    name = models.TextField(null=False, blank=False)
    email = models.TextField(null=False, blank=False)
    contact = models.TextField(null=False, blank=False)
    date_of_joining = models.DateTimeField(null=False, blank=False)
    experience = models.IntegerField(null=True, blank=True)
    department = models.ForeignKey('api.Department', on_delete=models.CASCADE,null=True,blank=False)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=False)

    def __str__(self):
        return self.name

class Role(models.Model):
    role_id = models.AutoField(primary_key=True,unique=True)
    name = models.TextField(null=False, blank=False)
    color = models.TextField(null=False,blank=False)
    permissions = models.CharField(max_length=20,choices=(('self',"SELF"),('manager','MANAGER'),('hr',)))

    def __str__(self):
        return self.name

class Department(models.Model):
    department_id = models.AutoField(primary_key=True,unique=True)
    name = models.TextField(null=False, blank=False)
    location = models.TextField(null=False, blank=False)
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE,null=True,blank=False,related_name="+")

    def __str__(self):
        return self.name

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(CustomUser)