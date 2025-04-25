from django.urls import path  #This line imports the path function from Django's urls module. The path function is used to define URL patterns for your application
from . import views  # imports the views module from the current package

 
urlpatterns = [

    path('', views.student_form, name='student_form'),
    path('list',views.student_list, name='student_list')
]