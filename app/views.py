from django.shortcuts import render,redirect
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView

class CropListAPIView(APIView):
    #1. List All Profiles
    def get(self, request, *args, **kwargs):

        all_instances = Crop.objects.all()
        serializer = CropSerializer(all_instances, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #2. Post an instance
    def post(self, request, *args, **kwargs):

        data = {
            'crop_name': request.data['crop_name'],
        }

        serializer = CropSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CropDetailAPIView(APIView):
    
    def get_object(self, id):

        try:
            return Crop.objects.get(id = id)
        except:
            return None
    
    #3. Get a particular instance
    def get(self, request, id, *args, **kwargs):

        instance = self.get_object(id)
        if instance is None:
            return Response(
                {'res': 'Object with model id does not exist'},
                status = status.HTTP_400_BAD_REQUEST,
            )

        serializer = CropSerializer(instance=instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #4. Update
    def put(self, request, id, *args, **kwargs):

        instance = self.get_object(id)
        if instance is None:
            return Response(
                {'res': 'Object with model id does not exist'},
                status = status.HTTP_400_BAD_REQUEST,
            )
        data = {
            'crop_name': request.data['crop_name'],   
        }
        serializer = CropSerializer(instance=instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #5. Delete
    def delete(self, request, id, *args, **kwargs):

        instance = self.get_object(id)
        if instance is None:
            return Response(
                {'res': 'Object with model id does not exist'},
                status = status.HTTP_400_BAD_REQUEST,
            )
        instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

class DistrictListAPIView(APIView):
    #1. List All Profiles
    def get(self, request, *args, **kwargs):

        all_instances = District.objects.all()
        serializer = DistrictSerializer(all_instances, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #2. Post an instance
    def post(self, request, *args, **kwargs):

        data = {
            'district_name': request.data['district_name'],
        }

        serializer = DistrictSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DistrictDetailAPIView(APIView):
    
    def get_object(self, id):

        try:
            return District.objects.get(id = id)
        except:
            return None
    
    #3. Get a particular instance
    def get(self, request, id, *args, **kwargs):

        instance = self.get_object(id)
        if instance is None:
            return Response(
                {'res': 'Object with model id does not exist'},
                status = status.HTTP_400_BAD_REQUEST,
            )

        serializer = DistrictSerializer(instance=instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #4. Update
    def put(self, request, id, *args, **kwargs):

        instance = self.get_object(id)
        if instance is None:
            return Response(
                {'res': 'Object with model id does not exist'},
                status = status.HTTP_400_BAD_REQUEST,
            )
        data = {
            'district_name': request.data['district_name'],   
        }
        serializer = CropSerializer(instance=instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #5. Delete
    def delete(self, request, id, *args, **kwargs):

        instance = self.get_object(id)
        if instance is None:
            return Response(
                {'res': 'Object with model id does not exist'},
                status = status.HTTP_400_BAD_REQUEST,
            )
        instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

class SoilListAPIView(APIView):

    #1. List All Profiles
    def get(self, request, *args, **kwargs):

        all_instances = Soil.objects.all()
        serializer = SoilSerializer(all_instances, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #2. Post an instance
    def post(self, request, *args, **kwargs):

        data = {
            'soil_name': request.data['soil_name'],
        }

        serializer = SoilSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SchemeListAPIView(APIView):

    #1. List All Profiles
    def get(self, request, *args, **kwargs):

        all_instances = Scheme.objects.all()
        serializer = SchemeSerializer(all_instances, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #2. Post an instance
    def post(self, request, *args, **kwargs):

        data = {
            'scheme_name': request.data['scheme_name'],
        }

        serializer = SchemeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnimalListAPIView(APIView):

    #1. List All Profiles
    def get(self, request, *args, **kwargs):

        all_instances = Animal.objects.all()
        serializer = AnimalSerializer(all_instances, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #2. Post an instance
    def post(self, request, *args, **kwargs):

        data = {
            'animal_name': request.data['animal_name'],
        }

        serializer = AnimalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AgriProductListAPIView(APIView):

    #1. List All Profiles
    def get(self, request, *args, **kwargs):

        all_instances = AgriProduct.objects.all()
        serializer = AgriProductSerializer(all_instances, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #2. Post an instance
    def post(self, request, *args, **kwargs):

        data = {
            'product_name': request.data['product_name'],
            'description' : request.data['description']
        }

        serializer = AgriProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CropDiseaseListAPIView(APIView):

    #1. List All Profiles
    def get(self, request, *args, **kwargs):

        all_instances = CropDisease.objects.all()
        serializer = CropDiseaseSerializer(all_instances, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #2. Post an instance
    def post(self, request, *args, **kwargs):

        recieved_data = {
            'crop_name': request.data['crop'],
            'disease_name' : request.data['disease_name'],
            'symptoms' : request.data['symptoms'],
            'identification_of_pathogen' : request.data['identification_of_pathogen'],
            'preventive_methods' : request.data['preventive_methods'],
        }

        #Checking if this crop is already in the table
        crop_name = recieved_data['crop_name']
        id = 0
        for crop in Crop.objects.all():
            if crop_name == crop.crop_name:
                id = crop.id

        #If the crop is not already in the databse then we need to add it 
        data = {
                'crop_name': crop_name
            }

        serializer = CropSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

        id = Crop.objects.last().id
        
        post_data = {
            'crop': id,
            'disease_name' : recieved_data['disease_name'],
            'symptoms' : recieved_data['symptoms'],
            'identification_of_pathogen' : recieved_data['identification_of_pathogen'],
            'preventive_methods' : recieved_data['preventive_methods'],
        }

        serializer = CropDiseaseSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CropGrowthListAPIView(APIView):

    #1. List All Profiles
    def get(self, request, *args, **kwargs):

        all_instances = CropDisease.objects.all()
        serializer = CropDiseaseSerializer(all_instances, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #2. Post an instance
    def post(self, request, *args, **kwargs):

        recieved_data = {
            'crop_name': request.data['crop'],
            'disease_name' : request.data['disease_name'],
            'symptoms' : request.data['symptoms'],
            'identification_of_pathogen' : request.data['identification_of_pathogen'],
            'preventive_methods' : request.data['preventive_methods'],
        }

        #Checking if this crop is already in the table
        crop_name = recieved_data['crop_name']
        id = 0
        for crop in Crop.objects.all():
            if crop_name == crop.crop_name:
                id = crop.id
        
        print(id)
        #If the crop is not already in the databse then we need to add it 
        if not id:
            data = {
                    'crop_name': crop_name
                }

            serializer = CropSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

            id = Crop.objects.last().id
        
        post_data = {
            'crop': id,
            'disease_name' : recieved_data['disease_name'],
            'symptoms' : recieved_data['symptoms'],
            'identification_of_pathogen' : recieved_data['identification_of_pathogen'],
            'preventive_methods' : recieved_data['preventive_methods'],
        }

        serializer = CropDiseaseSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)