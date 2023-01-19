from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Crop(models.Model):
    crop_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.crop_name

class District(models.Model):
    district_name = models.CharField(max_length=100, null=True, blank=True)

class Soil(models.Model):
    soil_name = models.CharField(max_length=100, null=True, blank=True)

class Scheme(models.Model):
    scheme_name = models.CharField(max_length=100, null=True, blank=True)

class Animal(models.Model):
    animal_name = models.CharField(max_length=100, null=True, blank=True)

class CropDisease(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, null=True, blank=True)
    disease_name = models.CharField(max_length=600, null=True, blank=True)
    symptoms = models.TextField( null=True, blank=True)
    identification_of_pathogen = models.TextField( null=True, blank=True)
    preventive_methods = models.TextField( null=True, blank=True)

    def __str__(self):
        return self.disease_name

class CropGrowth(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    production = models.CharField(max_length=100, null=True, blank=True)
    productivity = models.CharField(max_length=100, null=True, blank=True)

class AgriProduct(models.Model):
    product_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.product_name

class SoilTestingCentre(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

class SoilInfo(models.Model):
    soil = models.ForeignKey(Soil, on_delete=models.CASCADE, null=True, blank=True)
    district = models.ManyToManyField(District)
    crop = models.ManyToManyField(Crop)
    characteristics = models.TextField(null=True, blank=True)

class SoilAssistance(models.Model):
    type_of_assistance = models.TextField(null=True, blank=True)
    criteria = models.TextField(null=True, blank=True)
    scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE)

class CropAssistance(models.Model):
    type_of_assistance = models.TextField(null=True, blank=True)
    pricing = models.CharField(max_length=100, null=True, blank=True)
    scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE)

class Fertiliser(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    urea = models.CharField(max_length=100, null=True, blank=True)
    imported_urea = models.CharField(max_length=100, null=True, blank=True)

class AnimalBreed(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    common_name = models.CharField(max_length=100, null=True, blank=True)
    breed_name = models.CharField(max_length=100, null=True, blank=True)

class CattleDisease(models.Model):
    disease = models.CharField(max_length=100, null=True, blank=True)
    district = models.ManyToManyField(District)
    time_frame_for_epidemic = models.CharField(max_length=100, null=True, blank=True)






