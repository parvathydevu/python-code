from django.urls import path  #This line imports the path function from Django's urls module. The path function is used to define URL patterns for your application
from . import views  # imports the views module from the current package

 

urlpatterns = [

    path('', views.home, name='home'), # 127.0.0.1:8000/ -> run a function called home in views
    path('info/', views.info, name='info'),# 127.0.0.1:8000/info -> run another function info in views
    path('index',views.index, name='index') #127.0.0.1:8000/index->run html templates
]