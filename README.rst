Client for `Genderize.io <http://genderize.io/>`_ web service.

Basic usage
-----------

Import the `Genderize` class and call its `get` method with a list of names.

::

    from genderize import Genderize
    print Genderize().get(['James', 'Eva', 'Thunderhorse'])

::

    [{u'count': 1037, u'gender': u'male', u'name': u'James', u'probability': 0.99},
     {u'count': 234, u'gender': u'female', u'name': u'Eva', u'probability': 1.0},
     {u'gender': None, u'name': u'Thunderhorse'}]

Shell usage
-----------

If run as a script, takes a list of names on stdin, and prints them with their genders.

::

    echo "James\nEva\nThunderhorse" | python -m genderize

::

    James: male
    Eva: female
    Thunderhorse: None
