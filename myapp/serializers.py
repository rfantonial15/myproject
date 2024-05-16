from rest_framework import serializers
from .models import KeyLog

class KeyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyLog
        fields = '__all__'
