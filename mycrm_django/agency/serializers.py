from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Agency

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            
        )

class AgencySerializer(serializers.ModelSerializer):
    agents = UserSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Agency
        fields = (
            "id",
            "name",
            "agents",
            "created_by",
        )