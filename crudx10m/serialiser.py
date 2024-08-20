from rest_framework import serializers
from .models import DemographicDataTest

class DemographicDataTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemographicDataTest
        fields = '__all__'