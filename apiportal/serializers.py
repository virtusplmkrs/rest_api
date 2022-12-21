from .models import Home
from rest_framework import serializers


class HomeSerializer(serializers.HyperlinkedModelSerializer):
    # name = serializers.HyperlinkedModelSerializer()
    class Meta:
        model  = Home
        fields = ('name','alias',)
    