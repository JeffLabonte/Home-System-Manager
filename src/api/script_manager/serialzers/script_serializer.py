from uuid import uuid4

from django.db import transaction
from rest_framework import serializers

from api.script_manager.models import Script, ScriptExecution, GitRepo


class GitRepoSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(
        default=uuid4
    )
    repo_url = serializers.CharField(
        max_length=128,
        required=True,
    )
    version = serializers.CharField(required=True)

    class Meta:
        model = GitRepo
        fields = [
            'id',
            'repo_url',
            'version',
        ]
        default_fields = [
            'id',
            'repo_url',
            'version',
        ]
        read_only_fields = [
            'id',
        ]


class ScriptExecutionSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(
        default=uuid4,
        read_only=True,
    )
    git_repo = GitRepoSerializer()
    script_to_execute = serializers.CharField(
        required=True,
    )
    arguments = serializers.CharField(
        required=True,
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
    )

    repository = GitRepoSerializer()

    def create(self, validated_data):
        with transaction.atomic():
            repository = validated_data.pop('repository')
            git_repo = GitRepoSerializer().create(repository)
            script = Script(repository=git_repo, **validated_data)
            script.save()

        return script

    class Meta:
        model = Script
        fields = [
            'name',
            'repository',
            'last_date_modified',
            'creation_date',
        ]
        read_only_fields = [
            'last_date_modified'
            'creation_date ',
        ]
