from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from app1.models import StudentsRegistrationModel,State

class Students_Registration_Form(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name','last_name','gender','address','country','state','phone_number','email','password1','password2')
    def __init__(self,*args,**kwargs):
        super(Students_Registration_Form,self).__init__(*args,**kwargs)
        self.fields['country'].empty_label = 'Select'
        self.fields['state'].empty_label = 'Select'
        self.fields['state'].queryset = State.objects.none()


    