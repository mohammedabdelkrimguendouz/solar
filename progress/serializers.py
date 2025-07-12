from rest_framework import serializers
from .models import Progress

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = '__all__'
        
        extra_kwargs = {
            'notes': {'required': False},
        }
        
    
