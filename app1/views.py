from django.shortcuts import render, redirect
from  django.contrib import messages
from django.contrib.auth import get_user_model
from app1.models import StudentsRegistrationModel,Country_Model,State
from app1.form import Students_Registration_Form
def home(request):
    return render(request,'app1/home.html')

def insert_student_details(request):
    if request.method =='POST':
        form = Students_Registration_Form(request.POST)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        country = request.POST.get('country')
        state = request.POST.get('state')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        print(first_name)
        print(last_name)
        print(gender)
        print(address)
        print(country)
        print(state)
        print(phone_number)
        print(email)
        print(password)
        print(password1)

        print(form.is_valid())
        if form.is_valid():
            form.save()
            print('Record Inserted Successfully')
            messages.success(request,"Thanks for successfull Registration")
            return redirect('/')
        else:
            print('Not stored')
    else:
        form = Students_Registration_Form()

    return render (request,'app1/info.html',{'form':form})


def load_cities(request):
    country_id = request.GET.get('country')
    cities = State.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'app1/city_dropdown_list_options.html', {'cities': cities}) 