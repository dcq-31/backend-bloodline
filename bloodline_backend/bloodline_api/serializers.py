from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from bloodline_api.models import Dog, User

#
# User Serializer
#
class UserSerializer(serializers.ModelSerializer):
  dogs = serializers.PrimaryKeyRelatedField(many=True, queryset=Dog.objects.all())
  class Meta:
    model = User
    fields = ['id', 'username', 'first_name', 'last_name', 'email','dogs']

class UserRegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password']

#
# Dog Serializer
#
class DogSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dog
    fields = ['id', 'name', 'code', 'owner', 'date_birth', 'breed', 'partners', 'litters', 'siblings', 'created_at', 'update_at']
    

#
# Dog Serializer
#
class DogPutSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dog
    fields = ['name', 'code', 'date_birth', 'breed', 'partners', 'litters', 'siblings']
    

#
# Dog Create Serializer
#
class DogCreateSerializer(serializers.Serializer): 
  name = serializers.CharField()
  code = serializers.CharField(validators=[UniqueValidator(queryset=Dog.objects.all())])
  date_birth = serializers.DateTimeField()
  breed = serializers.ChoiceField(choices=Dog.DOGS_BREED_CHOICHES)
  
 
  def create(self, validated_data):
    return Dog.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.code = validated_data.get('code', instance.code)
    instance.date_birth = validated_data.get('date_birth', instance.date_birth)
    instance.breed = validated_data.get('breed', instance.breed)
    instance.owner = validated_data.get('owner', instance.owner)
    instance.save()
    return instance