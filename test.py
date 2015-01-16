from genderize import Genderize

def test_integration():
	"""
	Integration test from the readme. Calls the real genderize.io API server.
	"""
	expected_genders = {
		'James': 'male',
		'Eva': 'female',
		'Thunderhorse': None,
	}
	actual_genders = dict((elem['name'], elem['gender'])
					  	  for elem in Genderize().get(expected_genders.keys()))
	assert expected_genders == actual_genders
