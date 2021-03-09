from rest_framework import serializers
from Admins.models import CreatePractioner
from .models import Available

class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreatePractioner
        fields = '__all__'

class AvailableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Available
        fields = '__all__'