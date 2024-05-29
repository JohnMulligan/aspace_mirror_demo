from rest_framework import serializers
from recordkeeper.models import *

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'