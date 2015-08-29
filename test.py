from genderize import Genderize, GenderizeException


def test_integration():
    """
    Integration test from the readme. Calls the real Genderize.io API server.
    """
    expected_genders = {
        'James': 'male',
        'Eva': 'female',
        'Thunderhorse': None,
    }
    actual_genders = dict((elem['name'], elem['gender'])
                          for elem in Genderize().get(expected_genders.keys()))
    assert expected_genders == actual_genders,\
        "Expected {0}, got {1}".format(expected_genders, actual_genders)


def test_integration_single():
    """
    Retrieve a single name.
    """
    expected = 'male'
    actual = Genderize().get1('Peter')['gender']
    assert expected == actual,\
        "Expected {0}, got {1}".format(expected, actual)


def test_invalid_api_key():
    """
    Calls the API server with an invalid API key.
    Should result in an exception.
    """
    caught = False
    try:
        Genderize(api_key='invalid_api_key').get1('Peter')
    except GenderizeException:
        caught = True
    assert caught, "Expected a GenderizeException to be thrown"


def test_with_headers():
    """
    Retrieve a single name with response headers.
    """
    response = Genderize().get(['Peter'], retheader=True)
    assert response['data'][0]['name'] == 'Peter', "Expected name data to be returned"
    assert response['headers'], "Expected response headers to be returned"
    for header in ['X-Rate-Limit-Limit', 'X-Rate-Limit-Remaining', 'X-Rate-Reset']:
        assert header in response['headers'],\
            "Expected {0} header to be returned".format(header)
