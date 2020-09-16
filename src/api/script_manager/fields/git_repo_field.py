from rest_framework import serializers
from django.core.validators import URLValidator


class GitRepoField(serializers.CharField):
    error_messages = {
        'invalid_url': 'Enter a valid url',
    }

    def to_internal_value(self, data):
        super().to_internal_value(data=data)
        URLValidator(message=self.error_messages['invalid_url'])
        return data
