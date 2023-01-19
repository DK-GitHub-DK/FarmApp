from rest_framework import serializers
from.models import *

"""
Every Serializer has this naming scheme --> <Model_Name>Serializer 
"""

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = "__all__"

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"

class SoilSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"

class SchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"

class CropDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropDisease
        fields = "__all__"
    
class CropGrowthSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"

class AgriProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgriProduct
        fields = "__all__"

class SoilTestingCentreSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"

class SoilInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"

class SoilAssistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"

class CropAssistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"

class fertilizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"

class AnimalBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"

class CattleDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"
