# serializers.py
from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)



    class Meta:
        model = User
        fields = ['name', 'last_name', 'phone_number', 'password']

    # def validate(self, data):
    #     if data['password'] != data['confirm_password']:
    #         raise serializers.ValidationError('Passwords do not match')
    #     return data
    #
    # def create(self, validated_data):
    #     validated_data.pop('confirm_password')
    #     user = User.objects.create_user(**validated_data)
    #     return user



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone_number', 'name', 'last_name',]
