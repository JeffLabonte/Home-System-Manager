from django.db import models

# Create your models here.


class Script(models.Model):
    FILE_TYPE_CHOICES = [
        'bash',
        'py',
        'sh',
        'yaml',
        'yml',
    ]

    name = models.CharField(max_length=64, required=True)
    script = models.ForeignKey(
        'ScriptRevision',
        on_delete=models.CASCADE,
    )
    file_type = models.CharField(
        max_length=5,
        choices=FILE_TYPE_CHOICES,
        required=True
    )
    last_change = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ScriptRevision(models.Model):
    script_file = models.FileField(upload_to='scripts/')
    revision = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
