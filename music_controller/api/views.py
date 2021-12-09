from django.db.models import query
from django.shortcuts import render
from rest_framework import generics, serializers
from .serializers import RoomSerializer
from .models import Room
# Create your views here.

class RoomView(generics.CreateAPIView):
    querySet = Room.objects.all()
    serializer_class = RoomSerializer

