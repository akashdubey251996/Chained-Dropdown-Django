from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser

class Country_Model(models.Model):
    country = models.CharField(max_length=50)
    def __str__(self):
        return self.country

class State(models.Model):
    country = models.ForeignKey(Country_Model,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name



class StudentsRegistrationModel(AbstractUser):
    GENDER = (('F', 'Female',),('M', 'Male',),('O', 'Other',))
    email = models.EmailField(unique=True)
    fathers_name = models.CharField(max_length=25)
    gender = models.CharField(max_length=1,choices=GENDER,default=None)
    address = models.CharField(max_length=50)
    country = models.ForeignKey(Country_Model,on_delete=models.CASCADE)
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    phone_number = models.CharField(verbose_name="Phone Number",max_length=10)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]


    

    

