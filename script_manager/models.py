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

    class Meta:
        ordering = ['name', 'last_change']


class ScriptRevision(models.Model):
    script_file = models.FileField(upload_to='scripts/', required=True)
    revision = models.IntegerField(required=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['revision']

    def __str__(self):
        return f'Filename: {self.script_file.name},' \
               f' Revision: {self.revision},' \
               f' Create at ${self.created_at}'
