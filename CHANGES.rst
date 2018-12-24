Change Log
----------

0.3.1
~~~~~

2018-12-24

* Added missing ``setup.py`` classifier for Python 3.7.

0.3.0
~~~~~

2018-12-21

* Added support for `Requests connection/read timeouts <http://docs.python-requests.org/en/master/user/advanced/#timeouts>`_, with a default of 30 seconds.
* Now tested on Python 3.7.
* Added fix to ``.travis.yml`` for broken PyPI publishing. See `travis-ci/dpl #861 <https://github.com/travis-ci/dpl/issues/861>`_ and `Releasing build artifacts <https://docs.travis-ci.com/user/deployment/pypi/#releasing-build-artifacts>`_.

0.2.0
~~~~~

2018-05-15

* Now respects the API limit of 10 names per request, and will break up larger name lists into multiple API requests transparently. This closes `issue #6 <https://github.com/SteelPangolin/genderize/issues/6>`_, reported by `neginahoomi <https://github.com/neginahoomi>`_.
* Now tested on Python 3.6, PyPy 2, and PyPy 3 as well, and generates Codecov coverage reports.
* Dropped support for Python 2.6 and 3.2.
* Updated author's contact info.

0.1.5
~~~~~

2015-10-09

* Incorporated `vionemc <https://github.com/vionemc>`_'s patch for `optionally returning response headers <https://github.com/SteelPangolin/genderize/pull/5>`_. Anyone that wants to inspect the rate limit headers should set `retheader=True`.
* Now tested on Python 3.5 as well.

0.1.4
~~~~~

2015-06-21

* Switched to HTTPS endpoint.
* Incorporated `granteagon <https://github.com/granteagon>`_'s patch for `_fixtypes <https://github.com/SteelPangolin/genderize/pull/2>`_.
* Added support for paid API keys.
* Included Sphinx API docs.

0.1.3
~~~~~

2015-01-16

* Supports Python 2.6, 2.7, 3.2, 3.3, and 3.4.
* Added an integration test that calls the Genderize.io API server.
* Now using Travis CI.

0.1.2
~~~~~

2014-11-26

* Python 3 support.

0.1.1
~~~~~

2014-06-20

* Incorporated `oychang <https://github.com/oychang>`_'s `patch for handling non-JSON error responses <https://github.com/SteelPangolin/genderize/pull/1>`_.

0.1.0
~~~~~

2014-03-15

* Initial release.
