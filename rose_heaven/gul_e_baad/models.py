from django.db import models

# Create your models here.

class customer_tourist(models.Model):
    name = models.CharField(max_length=50,default="")
    father_name = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=50,default="")
    password = models.CharField(max_length=50,default="")
    age = models.CharField(max_length=50,default="")
    gender = models.CharField(max_length=50,default="")
    cnic = models.CharField(max_length=50,default="")
    phone_no  = models.CharField(max_length=11,default="")
    description  = models.TextField(max_length=50,default="")   
    def __str__(self):
        return self.name
    
    

class tour_package(models.Model):
    name = models.CharField(max_length=50,default="")
    phone_no  = models.CharField(max_length=11,default="")
    room_no = models.IntegerField(max_length=3,default="")
    days_of_stay = models.IntegerField(max_length=3,default="")
    tourpackagedetail = models.CharField(max_length=50,default="")
    transportdetail = models.CharField(max_length=50,default="")
    tourareadetail = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=50,default="")
    password = models.CharField(max_length=50,default="")
    age = models.CharField(max_length=50,default="")
    gender = models.CharField(max_length=50,default="")
    def __str__(self):
        return self.name
         
         
         
         
         
                    
class adeemaform_1(models.Model):
    name = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=50,default="")
    password = models.CharField(max_length=50,default="")
    age = models.CharField(max_length=50,default="")
    father_name = models.CharField(max_length=50,default="")
    datetime = models.CharField(max_length=50,default="")
    def __str__(self):
        return self.name
