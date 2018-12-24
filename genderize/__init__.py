"""
Client for Genderize.io web service.
"""

from collections import namedtuple
from itertools import chain, islice

import requests

__all__ = ['Genderize', 'GenderizeException']
__version__ = '0.3.1'


class GenderizeException(Exception):
    """
    Exception from Genderize.io web service.
    """


# Response from a single web service call.
_GenderizeResponse = namedtuple('_GenderizeResponse', ('data', 'headers'))


class Genderize(object):
    """
    Client for Genderize.io web service.
    Uses a Requests session for persistent HTTP connections.
    """

    # API requests are now limited to this many names per request.
    # https://genderize.io/#multipleusage
    BATCH_SIZE = 10

    def __init__(self, user_agent=None, api_key=None, timeout=30.0):
        """
        :param user_agent: Optional user agent string.
        :type user_agent: Optional[str]
        :param api_key: Optional API key.
        :type api_key: Optional[str]
        :param timeout: Optional connect/read timeout in seconds.
        :type timeout: Optional[float]
        """
        if user_agent is None:
            user_agent = 'Genderize/{0}'.format(__version__)

        self.api_key = api_key
        self.timeout = timeout

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

    def get(self, names, country_id=None, language_id=None, retheader=False):
        """
        Look up gender for a list of names.
        Can optionally refine search with locale info.
        May make multiple requests if there are more names than
        can be retrieved in one call.

        :param names: List of names.
        :type names: Iterable[str]
        :param country_id: Optional ISO 3166-1 alpha-2 country code.
        :type country_id: Optional[str]
        :param language_id: Optional ISO 639-1 language code.
        :type language_id: Optional[str]
        :param retheader: Optional
        :type retheader: Optional[boolean]
        :return:
        If retheader is False:
            List of dicts containing 'name', 'gender',
                     'probability', 'count' keys. If 'gender' is None,
                     'probability' and 'count' will be omitted.
        else:
            A dict containing 'data' and 'headers' keys.
            Data is the same as when retheader is False.
            Headers are the response header
            (a requests.structures.CaseInsensitiveDict).
            If multiple requests were made,
            the header will be from the last one.
        :rtype: Union[dict, Sequence[dict]]
        :raises GenderizeException: if API server returns HTTP error code.
        """
        responses = [
            self._get_chunk(name_chunk, country_id, language_id)
            for name_chunk
            in _chunked(names, Genderize.BATCH_SIZE)
        ]
        data = list(chain.from_iterable(
            response.data for response in responses
        ))
        if retheader:
            return {
                "data": data,
                "headers": responses[-1].headers,
            }
        else:
            return data

    def _get_chunk(self, name_chunk, country_id, language_id):
        """

        :type name_chunk: Iterable[str]
        :type country_id: Optional[str]
        :type language_id: Optional[str]
        :rtype:
        """
        params = [('name[]', name) for name in name_chunk]
        if self.api_key:
            params.append(('apikey', self.api_key))
        if country_id:
            params.append(('country_id', country_id))
        if language_id:
            params.append(('language_id', language_id))

        response = self.session.get(
            'https://api.genderize.io/',
            params=params,
            timeout=self.timeout)

        if 'application/json' not in response.headers.get('content-type', ''):
            status = "server responded with {http_code}: {reason}".format(
                http_code=response.status_code, reason=response.reason)
            raise GenderizeException(
                'response not in JSON format ({status})'.format(status=status),
                response.headers)

        decoded = response.json()
        if response.ok:
            # API returns a single object for a single name
            # but a list for multiple names.
            if not isinstance(decoded, list):
                decoded = [decoded]
            decoded = [self._fixtypes(data) for data in decoded]
            return _GenderizeResponse(data=decoded, headers=response.headers)
        else:
            raise GenderizeException(
                decoded['error'],
                response.status_code,
                response.headers)

    def get1(self, name, **kwargs):
        """
        Look up gender for a single name.
        See :py:meth:`get`.
        Doesn't support retheader option.
        """
        if 'retheader' in kwargs:
            raise GenderizeException(
                "get1() doesn't support the retheader option.")
        return self.get([name], **kwargs)[0]


def _chunked(iterable, n):
    """
    Collect data into chunks of up to length n.
    :type iterable: Iterable[T]
    :type n: int
    :rtype: Iterator[list[T]]
    """
    it = iter(iterable)
    while True:
        chunk = list(islice(it, n))
        if chunk:
            yield chunk
        else:
            return
