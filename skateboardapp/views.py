from skateboardapp.models import Skateboard
from skateboardapp.serializers import SkateboardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SkateboardList(APIView):
    def get(self, request, format=None):
        skateboard = Skateboard.objects.all()
        serializer = SkateboardSerializer(skateboard, many=True)
        return Response(serializer.data)