# Generated by Django 3.1.1 on 2020-09-14 04:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScriptRevision',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('script_file', models.FileField(upload_to='scripts/')),
                ('revision', models.IntegerField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['revision', 'creation_date', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('file_type', models.CharField(choices=[('bash', 'Bourne Again Shell Script'), ('py', 'Python Script'), ('sh', 'Shell Script'), ('yaml', 'YAML')], max_length=5)),
                ('last_date_modified', models.DateTimeField(auto_now=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('script', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='script_manager.scriptrevision')),
            ],
            options={
                'ordering': ['name', 'last_date_modified', 'creation_date'],
            },
        ),
    ]
