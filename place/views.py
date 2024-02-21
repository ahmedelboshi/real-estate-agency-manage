from django.shortcuts import render
from .models import Country , Governorate , City
from .serializers import CountrySerializer , GovernorateSerializer , CitySerializer
from rest_framework import viewsets , filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class Country(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class Governorate(viewsets.ModelViewSet):
    queryset = Governorate.objects.all()
    serializer_class = GovernorateSerializer
    filter_backends = [filters.SearchFilter , DjangoFilterBackend]
    filterset_fields = ['country']

class City(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [filters.SearchFilter , DjangoFilterBackend]
    search_fields = ['name_ar','name_en' ]
    filterset_fields = ['governorate']
