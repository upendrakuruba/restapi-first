from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import status
# Create your views here.
class resapi(viewsets.ModelViewSet):
    queryset=animal.objects.all()
    serializer_class=animalserializers