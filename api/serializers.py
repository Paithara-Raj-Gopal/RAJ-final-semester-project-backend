from rest_framework import serializers
from .models import HealthData  # Import your model

class HealthDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthData
        fields = '__all__'  # Include all fields

    def validate_stressLevel(self, value):
        if value not in ["Low", "Moderate", "High"]:
            raise serializers.ValidationError("Invalid stress level.")
        return value
