from rest_framework import serializers
from .models import User
import re


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_name(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("Name should not contain numbers.")
        return value

    def validate_surname(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("Surname should not contain numbers.")
        return value

    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Age must be a positive integer.")
        return value

    def validate_phone(self, value):
        phone_regex = re.compile(r'^\+?1?\d{9,15}$')
        if not phone_regex.match(value):
            raise serializers.ValidationError(
                "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
        return value

    def validate_username(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("Username should contain only alphanumeric characters.")
        return value