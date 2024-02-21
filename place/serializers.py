from rest_framework import serializers
from .models import Country , City , Governorate

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        exclude = ['status','governorate']
        #depth = 2

class GovernorateSerializer(serializers.ModelSerializer):
    # country = CountrySerializer()
    cities = CitySerializer(many=True)
    class Meta:
        model = Governorate
        exclude = ['status','country']

class CountrySerializer(serializers.ModelSerializer):
    governors = GovernorateSerializer(many=True)
    class Meta:
        model = Country
        exclude = ['status']
        depth = 4