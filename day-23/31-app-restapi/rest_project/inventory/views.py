from django.shortcuts import render # <- we don't render anything here
from rest_framework import viewsets
from .models import Consumable
from .serializers import ConsumableSerializer

# Create your views here.
class ConsumableViewSet(viewsets.ModelViewSet):

    queryset = Consumable.objects.all()
    serializer_class = ConsumableSerializer

'''

What is queryset?
    It tells DRF which data this view should operate on.
    Consumable.objects.all() means: “Use all rows from the Consumable table.”
    This data will be filtered automatically if you use features like .get(pk=id) or filtering/searching.

What is serializer_class?
    It tells DRF how to convert model instances to JSON and vice versa.
    ConsumableSerializer is the class that handles this.
    It controls what fields get included in the API response/request, and how data is validated.

'''