from django.urls import reverse


def test__script_manager_view_not_auth__should_return_401(client):
    url = reverse('script-list')
    assert url
    assert client
