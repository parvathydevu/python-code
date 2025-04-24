#REST API
from rest_framework import serializers
from .models import Consumable

class ConsumableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumable
        fields = '__all__'