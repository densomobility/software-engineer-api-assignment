from skateboardapp.models import Skateboard
from skateboardapp.serializers import SkateboardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SkateboardList(APIView):
    def get(self, request, format=None):
        skateboard = Skateboard.objects.all()
        serializer = SkateboardSerializer(skateboard, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SkateboardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SkateboardAvailable(APIView):
    def get(self, request, available, *args, **kwargs):
        skateboard = Skateboard.objects.all().filter(availability=available)
        serializer = SkateboardSerializer(skateboard, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
