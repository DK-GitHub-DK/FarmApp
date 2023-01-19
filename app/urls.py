from django.urls import path,include
from . import views

urlpatterns = [

    #Crop
    path('crop/', views.CropListAPIView.as_view()),
    path('crop/<int:id>/', views.CropDetailAPIView.as_view()),

    path('agri-product/', views.AgriProductListAPIView.as_view()),

    path('crop-disease/', views.CropDiseaseListAPIView.as_view()),
]