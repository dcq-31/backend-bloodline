from rest_framework import serializers
from .models import Dog, User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']

# Dog Serializer
class DogSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dog
    fields = ['id', 'name', 'code', 'user', 'date_birth', 'breed', 'partners', 'created_at', 'update_at']