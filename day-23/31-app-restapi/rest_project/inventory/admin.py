from django.contrib import admin
from .models import Consumable  #import the class in models.py

# Register your models here.
#step3
admin.site.register(Consumable)
