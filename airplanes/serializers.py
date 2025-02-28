from rest_framework import serializers
from .models import Airplane

class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ['id', 'tail_number', 'model', 'capacity', 'production_year', 'status']

    def validate_tail_number(self, value):
       
        request = self.context.get('request')  
        instance = getattr(self, 'instance', None)  
        if instance and instance.tail_number == value:
            return value  

        if Airplane.objects.filter(tail_number=value).exists():
            raise serializers.ValidationError("This tail number is already in use.")
        
        return value

    def validate_capacity(self, value):
       
        if value <= 0:
            raise serializers.ValidationError("Capacity must be greater than zero.")
        return value
