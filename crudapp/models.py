from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30,null=False,blank=False,verbose_name="First Name")
    last_name = models.CharField(max_length=30,null=False,blank=False,verbose_name="Last name")
    phone = models.CharField(max_length=10,null=False,blank=False,verbose_name="Phone Number")
    email = models.EmailField(max_length=277,null=False,blank=False,verbose_name="Email Address")
    address = models.TextField(max_length=100,verbose_name="Address")    
    def __str__(self):
        return str(self.id)
    

