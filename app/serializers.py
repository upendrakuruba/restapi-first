from rest_framework import serializers
from .models import *
class animalserializers(serializers.ModelSerializer):
    class Meta:
        model=animal
        fields='__all__'
