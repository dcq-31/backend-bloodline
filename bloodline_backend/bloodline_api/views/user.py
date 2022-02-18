from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from bloodline_api.models import User
from bloodline_api.serializers import UserSerializer, UserRegisterSerializer

#
# User Views
#
class UserList(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
 
class UserRegister(APIView):
  def post(self, request, format=None):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.save()
      token = Token.objects.create(user=user)
      return Response({"data": serializer.data, "token": token.key}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserDetail(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer