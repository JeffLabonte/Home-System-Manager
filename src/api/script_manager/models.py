from django.db import models

from uuid import uuid4


class ScriptExecution(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )
    git_repo = models.ForeignKey(
        "GitRepo",
        on_delete=models.CASCADE,
    )
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

    def __str__(self):
        return f"Running {self.script_to_execute} with {self.arguments} from {self.git_repo.repo_url}"


class GitRepo(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )
    repo_url = models.CharField(
        max_lenth=128,
        min_length=1,
        blank=False,
        null=False,
        unique=True,
    )
    version = models.IntegerField(blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            "revision",
            "creation_date",
            "id",
        ]

    def __str__(self):
        return f"Filename: {self.script_file.name}, Revision: {self.revision}, Create at ${self.creation_date}"


class Script(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )
    name = models.CharField(
        max_length=64,
        null=False,
        blank=False,
    )
    repository = models.ForeignKey(
        "GitRepo",
        on_delete=models.CASCADE,
    )
    last_date_modified = models.DateTimeField(auto_now=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            "name",
            "last_date_modified",
            "creation_date",
        ]
