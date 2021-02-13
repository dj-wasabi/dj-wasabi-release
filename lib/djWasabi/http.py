#!/usr/bin/env python

import sys
import requests
from . import generic
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from http.client import HTTPConnection


class request():
    """."""

    def __init__(
        self, debug: bool = False, status: list = None, methods: list = None, backoff: int = 1,
            retries: int = 5, timeout: int = 10):
        """Set defaults and setting up retry mechanism for http requests.

        :param debug: If we need debug information or not.
        :type debug: bool
        :param status: A list with http status code that needs to be retried.
        :type status: list
        :param methods: A list with htto methods that are allowed to be retried.
        :type methods: list
        :param retries: The amount of retries we want to use.
        :type retries: int
        :param backoff: The timeout in seconds
        :type backoff: int
        :param timeout: The timeout in seconds
        :type timeout: int
        """
        self.debug = debug
        self.timeout = timeout

        if methods is None:
            methods = ["HEAD", "GET", "PUT", "DELETE", "OPTIONS", "TRACE"]
        if status is None:
            status = [429, 500, 502, 503, 504]

        # https://findwork.dev/blog/advanced-usage-python-requests-timeouts-retries-hooks/
        retry_strategy = Retry(
            total=retries,
            status_forcelist=status,
            backoff_factor=backoff,
            allowed_methods=methods
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        http = requests.Session()
        http.mount("https://", adapter)
        http.mount("http://", adapter)

        if debug:
            HTTPConnection.debuglevel = 1
        self.http = http

    def _get(self, url: str = None, headers: dict = {}) -> tuple:
        """GET the information from provided url.

        :param url: The URL we want to GET.
        :type url: str
        :param headers: The headers.
        :type headers: dict
        :rtype: tuple
        :return: Succes (or not) with the request object
        """
        if not url:
            raise ValueError('Please provide the URL.')

        try:
            return (True, self.http.get(url, headers=headers, timeout=self.timeout))
        except requests.exceptions.RequestException as e:
            return (False, {'error': e})

    def _patch(self, url: str = None, headers: dict = {}, data: dict = {}) -> tuple:
        """PATCH the information from provided url.

        :param url: The URL we want to PATCH.
        :type url: str
        :param headers: The headers.
        :type headers: dict
        :param data: The headers.
        :type data: dict
        :rtype: tuple
        :return: Succes (or not) with the request object
        """
        if not url:
            raise ValueError('Please provide the URL.')

        try:
            return (True, self.http.patch(url, headers=headers, data=data, timeout=self.timeout))
        except requests.exceptions.RequestException as e:
            return (False, {'error': e})

    def _post(self, url: str = None, headers: dict = {}, data: dict = {}) -> tuple:
        """POST the information from provided url.

        :param url: The URL we want to POST.
        :type url: str
        :param headers: The headers.
        :type headers: dict
        :param data: The data we want to POST.
        :type data: dict
        :rtype: tuple
        :return: Succes (or not) with the request object
        """
        if not url:
            raise ValueError('Please provide the URL.')

        try:
            return (True, self.http.post(url, headers=headers, data=data, timeout=self.timeout))
        except requests.exceptions.RequestException as e:
            return (False, {'error': e})

    def _put(self, url: str = None, headers: dict = {}) -> tuple:
        """PUT the information from provided url.

        :param url: The URL we want to PUT.
        :type url: str
        :param headers: The headers.
        :type headers: dict
        :rtype: tuple
        :return: Succes (or not) with the request object
        """
        if not url:
            raise ValueError('Please provide the URL.')

        try:
            return (True, self.http.put(url, headers=headers, timeout=self.timeout))
        except requests.exceptions.RequestException as e:
            return (False, {'error': e})

    def _delete(self, url: str = None, headers: dict = {}) -> tuple:
        """DELETE the information from provided url.

        :param url: The URL we want to DELETE.
        :type url: str
        :param headers: The headers.
        :type headers: dict
        :rtype: tuple
        :return: Succes (or not) with the request object
        """
        if not url:
            raise ValueError('Please provide the URL.')

        try:
            return (True, self.http.delete(url, headers=headers, timeout=self.timeout))
        except requests.exceptions.RequestException as e:
            return (False, {'error': e})

    def verifyResponse(self, success: bool = False, data: dict = {}) -> dict:
        """Get the correct configuration for the repository.

        :param success: The status value of the http request.
        :type success: bool
        :param data: The compleet requests data object.
        :type data: dict
        :rtype: dict
        :return: The combination of the default and overriden config.
        """
        if success and data.ok:
            generic.debugLog(debug=self.debug, message="We have successful request, returning json data.")
            return data.json()
        else:
            error = {
                "status": data.status_code,
                "headers": data.headers,
                "url": data.url,
                "text": data.text
            }
            print(error)
            sys.exit(1)
