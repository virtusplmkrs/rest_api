from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HomeSerializer
from .models import Home


class HomeView(viewsets.ModelViewSet):
    queryset = Home.objects.all().order_by('name')
    
    serializer_class = HomeSerializer