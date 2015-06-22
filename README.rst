Genderize
---------

Client for `Genderize.io <https://genderize.io/>`_ web service.

.. image:: https://img.shields.io/pypi/v/Genderize.svg?style=flat
  :target: https://pypi.python.org/pypi/Genderize

.. image:: https://img.shields.io/pypi/dm/Genderize.svg?style=flat
  :target: https://pypi.python.org/pypi/Genderize

.. image:: https://img.shields.io/travis/SteelPangolin/genderize.svg?style=flat
  :target: https://travis-ci.org/SteelPangolin/genderize

.. image:: https://readthedocs.org/projects/genderize/badge/?style=flat
  :target: https://genderize.readthedocs.org/


Basic usage
-----------

Import the `Genderize` class and call its `get` method with a list of names.

::

    from genderize import Genderize
    print(Genderize().get(['James', 'Eva', 'Thunderhorse']))

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


Advanced usage
--------------

Create a `Genderize` instance with a custom user agent,
and an `API key <https://store.genderize.io/>`_.
Note that you'll need to use your own API key or this example won't work.

::

    from genderize import Genderize
    genderize = Genderize(
        user_agent='GenderizeDocs/0.0',
        api_key='example_api_key')
    print(genderize.get(['James', 'Eva', 'Thunderhorse']))

::

    [{u'count': 1037, u'gender': u'male', u'name': u'James', u'probability': 0.99},
     {u'count': 234, u'gender': u'female', u'name': u'Eva', u'probability': 1.0},
     {u'gender': None, u'name': u'Thunderhorse'}]
