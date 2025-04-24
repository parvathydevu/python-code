from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Student

# Create your views here.

@login_required
def student_form(request):
    print(request.POST)   # <- dictionary
    if(request.method == 'POST'):
        # collect the data from the form request
        name = request.POST.get('name', 'Unknown')
        age = request.POST.get('age', 'Unknown')
        class_name = request.POST.get('class_name', 'Unknown')
        marks = request.POST.get('marks', 'Unknown')
        # A row is creted in the model (table)
        Student.objects.create(name=name, age=age, class_name=class_name, marks=marks)
        # redirect to a different view
        return redirect('student_list')  # You can also skip this
    return render(request, 'students/student_form.html')

@login_required
def student_list(request):
    context = {
        'students': Student.objects.all()
    }
    return render(request, 'students/student_list.html', context)
#password-0000
#username-Parvathy