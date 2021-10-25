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
        skateboard = Skateboard.objects.all().filter(available=available)
        serializer = SkateboardSerializer(skateboard, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SkateboardOwner(APIView):
    def get(self, request, owner, *args, **kwargs):
        skateboard = Skateboard.objects.all().filter(owner=owner)
        serializer = SkateboardSerializer(skateboard, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SkateboardOwnerEntry(APIView):
    def get_object(self, owner, entry_id):
        try:
            return Skateboard.objects.all().filter(owner=owner, id=entry_id)
        except Skateboard.DoesNotExist:
            return None

    def get(self, request, owner, entry_id, *args, **kwargs):
        skateboard = self.get_object(owner, entry_id)
        if not skateboard:
            return Response(status.HTTP_400_BAD_REQUEST)
        serializer = SkateboardSerializer(skateboard, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, owner, entry_id):
        skateboard = self.get_object(owner, entry_id).first()
        if not skateboard:
            return Response(status.HTTP_400_BAD_REQUEST)
        serializer = SkateboardSerializer(skateboard, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, owner, entry_id):
        skateboard = self.get_object(owner, entry_id)
        skateboard.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK)
