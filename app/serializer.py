from rest_framework import serializers
from .models import RedZone

class RZSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = RedZone
        fields = "__all__"