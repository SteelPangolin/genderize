from genderize import Genderize


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
        "Expected {}, got {}".format(expected, actual)


def test_integration_single():
    """
    Retrieve a single name.
    """
    expected = 'male'
    actual = Genderize().get1('Peter')['gender']
    assert expected == actual,\
        "Expected {}, got {}".format(expected, actual)
