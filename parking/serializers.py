from rest_framework import serializers
from .models import Spots, Parked

class SpotsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spots
        fields = ('id', 'latitude', 'longitude', 'occupied')

class ParkedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parked
        fields = ('id', 'spot_id', 'time_slots')