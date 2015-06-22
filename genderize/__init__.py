"""
Client for Genderize.io web service.
"""

import requests

__all__ = ['Genderize', 'GenderizeException']
__version__ = '0.1.4'


class GenderizeException(Exception):
    """
    Exception from Genderize.io web service.
    """


class Genderize(object):
    """
    Client for Genderize.io web service.
    Uses a Requests session for persistent HTTP connections.
    """

    def __init__(self, user_agent=None, api_key=None):
        """
        :param user_agent: Optional user agent string.
        :type user_agent: string
        :param api_key: Optional API key.
        :type api_key: string
        """
        if user_agent is None:
            user_agent = 'Genderize/{0}'.format(__version__)

        self.api_key = api_key

        self.session = requests.Session()
        self.session.headers = {'User-Agent': user_agent}

    @staticmethod
    def _fixtypes(data):
        """
        'probability' key is clearly supposed to be a float,
        but is sent as a string.

        :type data: dict
        :rtype: dict
        :return: Same dict as input, modified in place.
        """
        if 'probability' in data:
            data['probability'] = float(data['probability'])
        return data

    def get(self, names, country_id=None, language_id=None):
        """
        Look up gender for a list of names.
        Can optionally refine search with locale info.

        :param names: List of names.
        :type names: Iterable[str]
        :param country_id: Optional ISO 3166-1 alpha-2 country code.
        :type country_id: Optional[str]
        :param language_id: Optional ISO 639-1 language code.
        :type language_id: Optional[str]
        :return: List of dicts containing 'name', 'gender',
                 'probability', 'count' keys. If 'gender' is None,
                 'probability' and 'count' will be omitted.
        :rtype: Sequence[dict]
        :raises GenderizeException: if API server returns HTTP error code.
        """
        params = [('name[]', name) for name in names]
        if self.api_key is not None:
            params.append(('apikey', self.api_key))
        if country_id:
            params.append(('country_id', country_id))
        if language_id:
            params.append(('language_id', language_id))

        response = self.session.get(
            'https://api.genderize.io/',
            params=params)

        if 'application/json' not in response.headers.get('content-type', ''):
            status = "server responded with {http_code}: {reason}".format(
                http_code=response.status_code, reason=response.reason)
            raise GenderizeException(
                'response not in JSON format ({status})'.format(status=status))

        decoded = response.json()
        if response.ok:
            # API returns a single object for a single name
            # but a list for multiple names.
            if not isinstance(decoded, list):
                decoded = [decoded]
            return self._fixtypes([self._fixtypes(data) for data in decoded])
        else:
            raise GenderizeException(decoded['error'], response.status_code)

    def get1(self, name, **kwargs):
        """
        Look up gender for a single name.
        See :py:meth:`get`.
        """
        return self.get([name], **kwargs)[0]
