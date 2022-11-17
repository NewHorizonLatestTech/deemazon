from django.db import models

# Create your models here.


class customer(models.Model):
    name = models.CharField(max_length=50,default="")
    father_name = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=50,default="")
    password = models.CharField(max_length=50,default="")
    age = models.CharField(max_length=50,default="")
    gender = models.CharField(max_length=50,default="")
    cnic = models.CharField(max_length=50,default="")
    phone_no  = models.CharField(max_length=11,default="")
    dececription = models.TextField(max_length=50,default="")   
    def __str__(self):
        return self.name

class foodpackage(models.Model):
    name = models.CharField(max_length=50,default="")
    phone_no  = models.CharField(max_length=11,default="")
    room_no = models.IntegerField(max_length=3,default="")
    days_of_stay = models.IntegerField(max_length=3,default="")
    foodpackagename = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=50,default="")
    password = models.CharField(max_length=50,default="")
    age = models.CharField(max_length=50,default="")
    gender = models.CharField(max_length=50,default="")
    def __str__(self):
        return self.name
