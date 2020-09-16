import re


from rest_framework import serializers


class GitRepositoryURLValidator:
    GIT_REGEX = re.compile(
        r'^(git\@)[a-z]+.((com)|(ca)):[a-z\/\-_]+(.git)$'
    )

    def is_valid(self, value):
        if isinstance(value, str):
            match = self.GIT_REGEX.search(value.lower())
            return match.group() if match else match

    def __call__(self, value):
        if not self.is_valid(value):
            message = "I expect a GIT or a HTTPS URL"
            raise serializers.ValidationError(message)
