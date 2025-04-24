from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello UST</h1>")
def info(request):
    return HttpResponse("<h1>My first Django program....</h1>")
def index(request):
    print(request.GET)  # Print the GET request parameters to the console
    dept = request.GET.get('dept')
    context = {
        'name': 'John Doe',
        'age': random.randint(1, 100),
        'dept': dept,
    }
    return render(request,'index.html',context) #name value pair -context
  #higher level function called render the request from index html