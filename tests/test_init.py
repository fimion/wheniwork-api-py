from wheniwork import raise_for_status_with_message
import pytest
import requests


def test_raise_for_status_with_message_no_error_on_successful_response():
    successful_response = requests.models.Response()
    successful_response.status_code = 200

    raise_for_status_with_message(successful_response)


def test_raise_for_status_with_message_shows_message_of_error():
    TEST_ERROR_MESSAGE = 'this should be in error message'
    EXPECTED_ERROR_MESSAGE = TEST_ERROR_MESSAGE
    error_500_response = requests.models.Response()
    error_500_response.status_code = 500
    error_500_response._content = TEST_ERROR_MESSAGE.encode('utf8')

    with pytest.raises(requests.exceptions.HTTPError) as excinfo:
        raise_for_status_with_message(error_500_response)
        assert EXPECTED_ERROR_MESSAGE in str(excinfo.value)

