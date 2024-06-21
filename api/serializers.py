from rest_framework import serializers
from api.models import movieapi

class movieapiserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=movieapi
        fields="__all__"
        