from django.urls import path
from app1 import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('add/',views.insert_student_details,name='add-student'),
    path('ajax/load-cities/',views.load_cities, name='ajax_load_cities'),

]
