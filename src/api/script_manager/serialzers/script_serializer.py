from uuid import uuid4

from rest_framework import serializers

from api.script_manager.models import Script, ScriptRevision
from api.script_manager.models import FILE_TYPE_CHOICES


class ScriptRevisionSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(default=uuid4)
    script_file = serializers.FileField(required=True)
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
        min_length=1,
    )

    script = ScriptRevisionSerializer()

    file_type = serializers.ChoiceField(
        choices=FILE_TYPE_CHOICES,
        required=True,
    )

    def create(self, validated_data):
        script_revision = ScriptRevision(**validated_data.pop('script'))
        script = Script(script=script_revision, **validated_data)
        script_revision.save()
        script.save()

        return script

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
