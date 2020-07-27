from django.db import models

# Create your models here.


class Script(models.Model):
    name = models.CharField(max_length=64, required=True)
    script = models.ForeignKey(
        'ScriptRevision',
        on_delete=models.CASCADE,
    )
    last_change = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ScriptRevision(models.Model):
    script_file = models.FileField(upload_to='scripts/')
    revision = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
