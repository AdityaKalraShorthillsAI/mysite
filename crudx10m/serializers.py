# from rest_framework import serializers
# from .models import DemographicDataTest, DemographicData


# class DemographicDataTestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DemographicDataTest
#         fields = '__all__'

# class DemographicDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DemographicData
#         fields = '__all__'


from rest_framework import serializers
from .models import WorkClass, Education, Occupation, MaritalStatus, NativeCountry, Race, Sex, Relationship, DemographicData

class WorkClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkClass
        fields = ['label']


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['label']


class OccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = ['label']


class MaritalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaritalStatus
        fields = ['label']


class NativeCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = NativeCountry
        fields = ['label']


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ['label']


class SexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sex
        fields = ['label']


class RelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        fields = ['label']


class DemographicDataSerializer(serializers.ModelSerializer):
    # workclass = serializers.CharField(source='workclass.label')
    # education = serializers.CharField(source='education.label')
    # occupation = serializers.CharField(source='occupation.label')
    # native_country = serializers.CharField(source='native_country.label')
    # race = serializers.CharField(source='race.label')
    # sex = serializers.CharField(source='sex.label')
    # relationship = serializers.CharField(source='relationship.label')
    # workclass = WorkClassSerializer()
    # education = EducationSerializer()
    # occupation = OccupationSerializer()
    # native_country = NativeCountrySerializer()
    # marital_status = MaritalStatusSerializer()
    # race = RaceSerializer()
    # sex = SexSerializer()
    # relationship = RelationshipSerializer()

    class Meta:
        model = DemographicData
        fields = '__all__'
