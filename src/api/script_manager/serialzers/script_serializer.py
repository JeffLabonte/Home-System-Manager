from uuid import uuid4

from rest_framework import serializers

from api.script_manager.models import Script, ScriptRevision
from api.script_manager.models import FILE_TYPE_CHOICES


class ScriptRevisionSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(default=uuid4)
    script_file = serializers.URLField(required=True)
    revision = serializers.IntegerField(required=True)

    class Meta:
        model = ScriptRevision
        fields = [
            'id',
            'script_file',
            'revision',
        ]
        default_fields = [
            'id',
            'script_file',
            'revision',
        ]


class ScriptSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
        max_length=64,
        min_length=12,
    )
    file_type = serializers.ChoiceField(
        choices=FILE_TYPE_CHOICES,
        required=True,
    )

    class Meta:
        model = Script
        fields = [
            'name',
            'script',
            'file_type',
            'last_date_modified',
            'creation_date',
        ]
        read_only_fields = [
            'last_date_modified'
            'creation_date ',
        ]
