from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
    )

    first_name = serializers.CharField(
        required=True,
    )

    last_name = serializers.CharField(
        required=True,
    )
    
    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'first_name',
            'last_name',
        ]
        default_fields = [
            'email',
            'first_name',
            'last_name',
        ]
