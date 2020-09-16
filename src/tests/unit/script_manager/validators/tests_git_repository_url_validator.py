import pytest
from rest_framework import serializers

from api.script_manager.validators.git_repository_url_validator import GitRepositoryURLValidator

INVALID_REPOS = [
    'something_wrong',
    1,
    'it@test.com:JeffLabonte/ThisDood.git',
    'git@test.com:JeffLabonte/ThisDood.gt',
    'git@test.com:JeffLabonte/',
    'git@test.com:JeffLabonte',
]


@pytest.mark.parametrize('repo', INVALID_REPOS)
def test_git_repo_field__invalid_input__should_raise_validation_exception(repo):
    with pytest.raises(serializers.ValidationError):
        GitRepositoryURLValidator()(repo)


def test_git_repository_url_validator__valid_input__should_work():
    GitRepositoryURLValidator()('git@github.com:JeffLabonte/Home-System-Manager.git')
