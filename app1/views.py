from django.shortcuts import render
from  django.contrib import messages
from django.contrib.auth import get_user_model
from app1.form import Students_Registration_Form
def home(request):
    return render(request,'app1/home.html')

def insert_student_details(request):
    if request.method =='POST':
        form = Students_Registration_Form(request.POST)

        if form.is_valid():
            form.save()
            print('Record Inserted Successfully')
            messages.success(request,"Thanks for successfull Registration")
            return redirect('/')
    else:
        form = Students_Registration_Form()

    return render (request,'app1/info.html',{'form':form})