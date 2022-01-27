from rest_framework import serializers
from .models import Dog, User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
  dogs = serializers.PrimaryKeyRelatedField(many=True, queryset=Dog.objects.all())
  class Meta:
    model = User
    fields = ['id', 'username', 'first_name', 'last_name', 'email','dogs']

# Dog Serializer
class DogSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dog
    fields = ['id', 'name', 'code', 'owner', 'date_birth', 'breed', 'partners', 'litters', 'siblings', 'created_at', 'update_at']