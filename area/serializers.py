from rest_framework import serializers

from area.models import DhakaSubArea


class DhakaSubAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DhakaSubArea
        fields = ['id', 'name', 'bn_name', 'lat', 'lng']

