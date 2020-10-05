from uuid import uuid4

from rest_framework import serializers

from api.script_manager.models import Script, ScriptExecution, GitRepo
from api.script_manager.models import FILE_TYPE_CHOICES


class GitRepoSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(
        default=uuid4
    )
    repo_url = models.CharField(
        max_lenth=128,
        min_length=1,
        blank=False,
        null=False,
        unique=True,
    )
    revision = serializers.IntegerField(required=True)

    class Meta:
        model = GitRepo
        fields = [
            'id',
            'script_file',
            'revision',
            'last_date_modified',
            'creation_date'
        ]
        default_fields = [
            'id',
            'script_file',
            'revision',
        ]
        read_only_fields = [
            'id',
        ]


class ScriptExecutionSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(
        default=uuid4,
        required=True,
        read_only=True,
    )
    git_repo = GitRepoSerializer()
    script_to_execute = models.CharField(
        min_length=1,
        blank=False,
        null=False,
    )
    arguments = models.CharField(
        min_length=1,
        blank=False,
        null=False,
    )

    class Meta:
        model = ScriptExecution
        fields = [
            'id',
            'git_repo',
            'script_to_execute',
            'arguments',
        ]


class ScriptSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
        max_length=64,
        min_length=1,
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
