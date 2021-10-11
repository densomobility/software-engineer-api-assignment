from rest_framework import serializers
from .models import SkateBoard

# defines the content shown on the APIs and validates the input against the conditions specified in the database schema(SkateBoard)
class SkateBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = SkateBoard
        fields = ['id', 'name_owner', 'brand', 'weight', 'length', 'location', 'timestamp', 'status']