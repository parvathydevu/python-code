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
def check(request):
    context = {
        'name': 'DEVIKA P',
        'age': str(random.randint(1, 100))
    }
    return render(request,'age_check.html',context) #name value pair -context
def fruit_list(request):
    fruitsList = ['Apple', 'Banana', 'Cherry', 'Dates', 'Orange']
    random.shuffle(fruitsList)
    context = {
        'name': 'John Doe',
        'age': str(random.randint(1, 30)),
        'fruits': fruitsList,
    }
    return render(request, 'fruit_list.html', context)
    
def input_form(request):
    return render(request, 'input.html')

def result(request):
    print(request.method)
    print(request.POST)
    if request.method == 'POST': 
        name = request.POST.get('name', 'Unknown')  #get() for dictionary ,key called name
        age = request.POST.get('age', 'Unknown') #request.POST['name'] is dictionaries
        context = {
            'name': name,
            'age' : age
        }
        return render(request, 'output.html', context) #if we post the name and age , it will goes to output result html
    else:
        return render(request, 'input.html', context)
def calculator(request):
    
    result = None
    
    if request.method == "POST":
        
        try:
            a = float(request.POST.get('a'))
            b = float(request.POST.get('b'))
            op = request.POST.get('operation')

            if op == 'add':
                result = a + b
            elif op == 'subtract':
                result = a - b
            elif op == 'multiply':
                result = a * b
            else:
                result = a / b if b != 0 else "Infinity"
        except Exception as e:
            result = f"Error: {str(e)}"

    context = {
        'result': result
    }
    return render(request, 'calculator.html', context)
def converter(request):
    result = None
    if request.method == "POST":
        try:
            inr_amount = float(request.POST.get('inr'))
            conversion_rate = 0.012 # Example conversion rate from INR to USD
            usd_amount = inr_amount * conversion_rate
            result = f"{inr_amount} INR = {usd_amount:.2f} USD"
        except Exception as e:
            result = f"Error: {str(e)}"
    context = {
                'result': result
    }
    return render(request, 'converter.html', context)

def timer(request):
    return render(request, 'timer.html')


