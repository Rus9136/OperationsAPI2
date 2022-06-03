from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Types, Costs
from django.forms.models import model_to_dict
from .serializers import CostSerializers
from rest_framework import viewsets, routers
from rest_framework.decorators import action



class CostViewSet(viewsets.ModelViewSet):
    queryset = Costs.objects.all()
    serializer_class = CostSerializers



router = routers.DefaultRouter()
router.register(r'cost', CostViewSet)

