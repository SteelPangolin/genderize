Genderize
---------

Client for the `Genderize.io <https://genderize.io/>`_ web service.

.. image:: https://img.shields.io/github/license/steelpangolin/genderize.svg?style=flat
  :target: https://github.com/SteelPangolin/genderize

.. image:: https://img.shields.io/pypi/v/Genderize.svg?style=flat
  :target: https://pypi.python.org/pypi/Genderize

.. image:: https://img.shields.io/travis/SteelPangolin/genderize.svg?style=flat
  :target: https://travis-ci.org/SteelPangolin/genderize

.. image:: https://img.shields.io/codecov/c/github/SteelPangolin/genderize.svg?style=flat
  :target: https://codecov.io/gh/SteelPangolin/genderize

.. image:: https://readthedocs.org/projects/genderize/badge/?style=flat
  :target: https://genderize.readthedocs.org/


Basic usage
-----------

Import the ``Genderize`` class and call its ``get`` method with a list of names.

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

Create a ``Genderize`` instance with a custom user agent,
an `API key <https://store.genderize.io/>`_,
and a shorter timeout than the default 30 seconds.
Note that you'll need to use your own API key or this example won't work.

::

    from genderize import Genderize
    genderize = Genderize(
        user_agent='GenderizeDocs/0.0',
        api_key='example_api_key',
        timeout=5.0)
    print(genderize.get(['James', 'Eva', 'Thunderhorse']))

::

    [{u'count': 1037, u'gender': u'male', u'name': u'James', u'probability': 0.99},
     {u'count': 234, u'gender': u'female', u'name': u'Eva', u'probability': 1.0},
     {u'gender': None, u'name': u'Thunderhorse'}]


Maintenance
-----------

Setup for local development:

::

    virtualenv --prompt '(genderize) ' venv -p python3
    pip install -r requirements.txt
    pip install -r requirements-dev.txt


Release checklist:

#. Generate a new version number: ``major.minor.micro``. It should be compatible with both `PEP 440 <https://www.python.org/dev/peps/pep-0440/>`_ and `SemVer 2.0.0 <https://semver.org/>`_.
#. Update ``__version__`` in ``genderize/__init__.py``. This is read by ``setup.py`` and doesn't need to be changed there.
#. Add a changelog entry and date for the new version in ``CHANGES.rst``.
#. Commit the changes. This may be done as part of another change.
#. Tag the commit with ``git tag major.minor.micro``.
#. Push the tag to GitHub with ``git push origin major.minor.micro``.
#. Travis will create a new PyPI release from the tag.
