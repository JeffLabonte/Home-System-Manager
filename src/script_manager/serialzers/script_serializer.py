from rest_framework import serializers
from script_manager.models import Script


class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Script
        fields = [
            'name',
            'script',
            'file_type',
        ]
