from rest_framework import serializers

from area.models import DhakaSubArea


class DhakaSubAreaSerializer(serializers.ModelSerializer):

    def unique_name(value):
        city = DhakaSubArea.objects.filter(name=value)
        if city.exists():
            raise serializers.ValidationError("This City is already exists.")

    name = serializers.CharField(max_length=150, validators=[unique_name])
    class Meta:
        model = DhakaSubArea
        fields = ['id', 'name', 'bn_name', 'lat', 'lng']

