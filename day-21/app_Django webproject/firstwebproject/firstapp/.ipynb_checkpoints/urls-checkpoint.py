from django.urls import path  #This line imports the path function from Django's urls module. The path function is used to define URL patterns for your application
from . import views  # imports the views module from the current package

urlpatterns = [

    path('', views.home, name='home'), # 127.0.0.1:8000/ -> run a function called home in views
    path('info/', views.info, name='info'),# 127.0.0.1:8000/info -> run another function info in views
    path('index',views.index, name='index'), #127.0.0.1:8000/index->run html templates and style css file
    path('check',views.check, name='check'),#127.0.0.1:8000/check
    path('fruits',views.fruit_list, name='fruits'),#127.0.0.1:8000/fruits
    path('input', views.input_form, name='input'), # 127.0.0.1:8000/input--post name age--goes to result
    path('result', views.result, name='result'), # 127.0.0.1:8000/result
    path('calculator', views.calculator, name='calculator'), # 127.0.0.1:8000/calculator
    path('converter',views.converter, name='converter'),# 127.0.0.1:8000/converter
    path('timer',views.timer, name='timer'),#127.0.0.1:8000/timers
]