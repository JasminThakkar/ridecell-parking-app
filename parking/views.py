from django.shortcuts import render
from parking.models import Spots, Parked
from parking.serializers import SpotsSerializer, ParkedSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
import django_filters
from django_filters import rest_framework as filters
from rest_framework import generics

# url = http://127.0.0.1:8000/spotsavailable/
# gets all spots which are unoccupied
class ListedSpots(APIView):
    def get(self, request, format=None):
        print(request.data)
        spots = Spots.objects.filter(occupied=False)
        serializer = SpotsSerializer(spots, many=True)
        return Response(serializer.data)
    #new parking spot reservation
    def post(self,request,format=None):
        print(request.data["spot_id"])
        print(ReservedSpot.get(self, request,request.data["spot_id"]))
        serializer = ParkedSerializer(data=request.data)
        if ReservedSpot.get(self, request,request.data["spot_id"]):
            if serializer.is_valid():
                serializer.save()
                return redirect('/parked/')
        content = {
            'message': "Requested Spot is not available"
        }
        return Response(content, data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# url = http://127.0.0.1:8000/spotsnearby/latitude=200&longitude=600&r=30
# gets spot near you by giving radius and your lat , log
class SpotinRadius(APIView):

    def get(self, request, latitude, longitude, r, format=None):
        filter_backends = (filters.DjangoFilterBackend,)
        lat, log, r = map(int,[latitude, longitude, r])
        latrange, logrange = [lat-r, lat+r], [log-r, log+r]# created range of given lat, log
        print(latrange,logrange)
        spots = Spots.objects.all()# getting all spots objects
        serializer = SpotsSerializer(spots, many=True)
        spotlist = []
        for spot in serializer.data:
            print(spot["latitude"], spot["longitude"])
            # finding spot in latrange and logrange
            if spot["latitude"] >= lat-r and spot["latitude"] <= lat+r and spot["longitude"] >= log-r and spot["longitude"] <= log+r:
                print(spot)
                spotlist.append(spot)
        return Response(spotlist)

# url = http://127.0.0.1:8000/reservedspots/
class ReservedSpot(APIView):
    def get(self, request, format=None):
        spots = Spots.objects.filter(occupied=True)
        serializer = SpotsSerializer(spots, many=True)
        return Response(serializer.data)

# url = http://127.0.0.1:8000/occupiedspots/
class OccupiedSpots(APIView):
    def get(self, request, format=None):
        parked = Parked.objects.all()
        serializer = ParkedSerializer(parked, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print (request.data["spot_id"])
        #print (ReserveIT.get(self, request, pk = request.data["spot_id"]))
        serializer = ParkedSerializer(data=request.data)
        if OccupiedSpots.get(self, request,request.data["spot_id"]):
            if serializer.is_valid():
                serializer.save()
                return redirect('/parked/')
        content = {
            'message': "Requested Spot is not available"
        }
        return Response(content, data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
