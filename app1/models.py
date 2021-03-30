from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser

class Country_Model(models.Model):
    country = models.CharField(max_length=10)
    def __str__(self):
        return self.country

class State(models.Model):
    country = models.ForeignKey(Country_Model,on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name


SEX = (('F', 'Female',),('M', 'Male',),('O', 'Other',))
class StudentsRegistrationModel(AbstractUser):
    email = models.EmailField(verbose_name='Email',unique=True)
    fathers_name = models.CharField(max_length=25)
    sex = models.CharField(max_length=1,choices=SEX)
    address = models.CharField(max_length=50)
    country = models.ForeignKey(Country_Model,on_delete=models.CASCADE)
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    dob = models.DateField(max_length=8)
    phone_number = models.CharField(verbose_name="Please don't include country code",max_length=10)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)

    USERNAME_FIELD = 'email'


    

    

