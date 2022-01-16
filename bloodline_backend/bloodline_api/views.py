from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Dog, User
from .serializers import DogSerializer, UserSerializer

# Dogs Views
class DogList(APIView):
  # List all dogs or create a new dog
  def get(self, request, format=None):
    dogs = Dog.objects.all()
    serializer = DogSerializer(dogs, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = DogSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DogDetail(APIView):
  # Retrieve, update or delete a dog.
  def get_object(self, pk):
    try:
      dog = Dog.objects.get(pk=pk)
      return dog
    except Dog.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    dog = self.get_object(pk)
    
    serializer = DogSerializer(dog)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    dog = self.get_object(pk)
    serializer = DogSerializer(dog, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

  def delete(self, request, pk, format=None):
    dog = self.get_object()
    dog.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)