from django.db import models

from uuid import uuid4

FILE_TYPE_CHOICES = [
    ('bash', 'Bourne Again Shell Script'),
    ('py', 'Python Script'),
    ('sh', 'Shell Script'),
    ('yaml', 'YAML'),
]


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
    script = models.OneToOneField(
        'ScriptRevision',
        on_delete=models.CASCADE,
        unique=True,
        null=False,
    )
    file_type = models.CharField(
        max_length=5,
        choices=FILE_TYPE_CHOICES,
        null=False,
    )
    last_date_modified = models.DateTimeField(auto_now=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            'name',
            'last_date_modified',
            'creation_date',
        ]


class ScriptRevision(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )
    script_file = models.URLField(
        blank=False,
        null=False,
        unique=False,
    )
    revision = models.IntegerField(blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            'revision',
            'creation_date',
            'id',
        ]

    def __str__(self):
        return f'Filename: {self.script_file.name},' \
               f' Revision: {self.revision},' \
               f' Create at ${self.creation_date}'
