from django.shortcuts import render
from .models import Lotr
from rest_framework import viewsets, permissions
from .serializer import LotrSerializer
# Create your views here.
class LotrViewSet(viewsets.ModelViewSet):
    queryset=Lotr.objects.all()
    serializer_class=LotrSerializer
    permission_classes=[permissions.AllowAny]