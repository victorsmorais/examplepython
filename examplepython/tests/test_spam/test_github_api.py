from unittest.mock import Mock

import pytest
from pytest_mock import mocker

from examplepython import github_api


@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/73318711?v=4'
    resp_mock.json.return_value = {
        'login': 'victorsmorais', 'id': 73318711,
        'avatar_url': url
    }
    get_mock = mocker.patch('examplepython.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('victorsmorais')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('victorsmorais')
    assert 'https://avatars.githubusercontent.com/u/73318711?v=4' == url
