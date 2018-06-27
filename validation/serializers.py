from django.contrib.auth.models import User
from .models import SimpleData
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = ('id', 'username', 'email')


# class Inventoryserializer(serializers.ModelSerializer):
#     class Meta:
#         model=Inventory
#         data = serializers.Field()
#         fields=('data')

class SimpleDataSerializer(serializers.ModelSerializer):
    data = serializers.ListField

    class Meta:
        model = SimpleData
        fields = ["data"]