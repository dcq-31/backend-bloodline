from rest_framework import generics
from bloodline_api.models import User
from bloodline_api.serializers import UserSerializer

#
# User Views
#
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer