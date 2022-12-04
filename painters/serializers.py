from rest_framework import serializers
from painters.models import Painting
from painters.models import Painting


class ImageCreateSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Painting
        fields = "__all__"
        read_only_fields=["user"]
        
class ConvertSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Painting
        fields = ("painting",)
        
