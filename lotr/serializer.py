from .models import Lotr
from rest_framework import serializers

class LotrSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Lotr
        fields='__all__'