from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from bloodline_api.models import Dog
from bloodline_api.serializers import DogSerializer, DogCreateSerializer, DogPutSerializer
from bloodline_api.permissions import IsOwnerOrReadOnly

#
# Dogs Views
#
class DogList(APIView):
  """
  List all dogs or create a new dog
  """
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
  def get(self, request):
    dogs = Dog.objects.all()
    serializer = DogSerializer(dogs, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = DogCreateSerializer(data=request.data)
    if serializer.is_valid():
      dog = serializer.save(owner=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DogDetail(APIView):
  """
  Retrieve, update or delete a dog.
  """
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
  
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
    self.check_object_permissions(request, dog)
    serializer = DogPutSerializer(dog, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

  def delete(self, request, pk, format=None):
    dog = self.get_object(pk)
    self.check_object_permissions(request, dog)
    dog.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
