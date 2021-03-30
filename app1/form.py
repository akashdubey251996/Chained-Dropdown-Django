from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from app1.models import Student_Registration_Model

class Students_Registration_Form(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name','last_name','dob','sex',' address','country','state','phone_number','email','password1','password2')



