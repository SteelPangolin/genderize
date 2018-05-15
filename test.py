# noinspection PyProtectedMember
from genderize import Genderize, GenderizeException, _chunked


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
    assert response['data'][0]['name'] == 'Peter',\
        "Expected name data to be returned"
    assert response['headers'], "Expected response headers to be returned"
    expected_headers = [
        'X-Rate-Limit-Limit',
        'X-Rate-Limit-Remaining',
        'X-Rate-Reset',
    ]
    for header in expected_headers:
        assert header in response['headers'],\
            "Expected {0} header to be returned".format(header)


def test_chunked_full_blocks():
    """
    Test chunking when the input length is a multiple of the block length.
    """
    chunks = list(_chunked("abcd", 2))
    assert len(chunks) == 2
    assert len(chunks[0]) == 2
    assert len(chunks[1]) == 2


def test_chunked_uneven_blocks():
    """
    Test chunking when the input length isn't a multiple of the block length.
    """
    chunks = list(_chunked("abcde", 2))
    assert len(chunks) == 3
    assert len(chunks[0]) == 2
    assert len(chunks[1]) == 2
    assert len(chunks[2]) == 1


def test_chunked_empty():
    """
    Test chunking when the input is empty.
    """
    chunks = list(_chunked("", 2))
    assert len(chunks) == 0


def test_more_than_10_names():
    """
    Retrieve 20 names, which requires multiple HTTP requests
    now that the API has a 10-name limit.
    """
    names = [
        "Emma",
        "Olivia",
        "Ava",
        "Isabella",
        "Sophia",
        "Mia",
        "Charlotte",
        "Amelia",
        "Evelyn",
        "Abigail",
        "Liam",
        "Noah",
        "William",
        "James",
        "Logan",
        "Benjamin",
        "Mason",
        "Elijah",
        "Oliver",
        "Jacob",
    ]
    response = Genderize().get(names)
    assert len(names) == len(response)
    for name, namedata in zip(names, response):
        assert name == namedata['name'],\
            'Expected names to be returned in same order'
