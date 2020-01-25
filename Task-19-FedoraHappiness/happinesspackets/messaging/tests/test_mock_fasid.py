import json
from django.test.client import RequestFactory
from ..views import FasidSearchView, AccountSystem
import pytest


@pytest.fixture(scope="function")
def call_fasid_check_and_get_response(mocker, mock_response):
    factory = RequestFactory()
    request = factory.get('/send/search/', {'fasid': 'mockuser'})
    request.session = {}  # hack for session middleware
    mocker.patch.object(AccountSystem, 'person_by_username', return_value=mock_response)
    return FasidSearchView.fasidCheck(request)


@pytest.fixture(scope="function")    
def call_fasid_check_and_get_server_error(mocker):
    factory = RequestFactory()
    request = factory.get('/send/search/', {'fasid': 'mockuser'})
    request.session = {}
    mocker.patch.object(AccountSystem, 'person_by_username', side_effect=KeyError('human_name'))
    return FasidSearchView.fasidCheck(request)


@pytest.mark.parametrize("mock_response", [{'privacy': False, 'email': 'mockuser@example.com', 'human_name': 'Mock User'}])
def test_fasid_check_returns_email_name_and_privacy(call_fasid_check_and_get_response):
    
    response = call_fasid_check_and_get_response
    expected_response = {
        'privacy': False,
        'email': 'mockuser@example.com',
        'name': 'Mock User'
    }

    assert response.status_code == 200
    assert json.loads(response.content) == expected_response


@pytest.mark.parametrize("mock_response", [{'privacy': True, 'email': 'mockuser@example.com', 'human_name': 'None'}])
def test_fasid_check_returns_null_in_name_when_user_has_set_privacy_to_true(call_fasid_check_and_get_response):
    
    response = call_fasid_check_and_get_response
    expected_response = {
        'privacy': True,
        'email': 'mockuser@example.com',
        'name': 'None'
    }

    assert response.status_code == 200
    assert json.loads(response.content) == expected_response


@pytest.mark.parametrize("mock_response", [None])
def test_fasid_check_returns_404_when_fas_id_does_not_exist(call_fasid_check_and_get_response):

    response = call_fasid_check_and_get_response
    expected_response = {'error': 'The FAS username does not exist!'}

    assert response.status_code == 404
    assert json.loads(response.content) == expected_response


def test_fasid_check_returns_500_for_an_unhandled_exception(call_fasid_check_and_get_server_error):

    response = call_fasid_check_and_get_server_error
    expected_response = {'error': 'Internal Server Error'}

    assert response.status_code == 500
    assert json.loads(response.content) == expected_response
