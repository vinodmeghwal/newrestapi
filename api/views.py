from django.shortcuts import render
from .serializers import movieapiserializer
from .models import movieapi
from rest_framework import routers , viewsets
# Create your views here.

class movieviewset(viewsets.ModelViewSet):
    queryset=movieapi.objects.all()
    serializer_class=movieapiserializer
