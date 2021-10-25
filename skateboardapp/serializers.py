from rest_framework import serializers
from skateboardapp.models import Skateboard

class SkateboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skateboard
        fields = "__all__"