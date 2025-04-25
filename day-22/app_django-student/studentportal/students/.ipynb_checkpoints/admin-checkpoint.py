from django.contrib import admin
from .models import Student


# Register your models here.very power ful tool
#allows you to control models-data from models(entire database)
#admin.site.register(Student) #class name
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):  #customising the admin display itself
    list_display =('name','age','class_name','marks')
    list_filter=('class_name',)
    ordering =('name',)