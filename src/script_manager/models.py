from django.db import models

from uuid import uuid4

# Create your models here.


class Script(models.Model):
    FILE_TYPE_CHOICES = [
        ('bash', 'Bourne Again Shell Script'),
        ('py', 'Python Script'),
        ('sh', 'Shell Script'),
        ('yaml', 'YAML'),
    ]

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
    last_change = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name', 'last_change']


class ScriptRevision(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )
    script_file = models.FileField(
        upload_to='scripts/',
        blank=False,
        null=False,
        unique=True,
    )
    revision = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['revision', 'id']

    def __str__(self):
        return f'Filename: {self.script_file.name},' \
               f' Revision: {self.revision},' \
               f' Create at ${self.created_at}'
