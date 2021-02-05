#!/usr/bin/env python

import sys
import requests
from . import generic


def _get(url: str = None, headers: dict = None, timeout: str = "10") -> tuple:
    """GET the information from provided url.

    :param url: The URL we want to GET.
    :type url: str
    :param headers: The headers.
    :type headers: dict
    :param timeout: The timeout in seconds
    :type timeout: str
    :rtype: tuple
    :return: Succes (or not) with the return object
    """
    if not url:
        raise ValueError('Please provide the URL.')
    if not headers:
        headers = {}

    try:
        return (True, requests.get(url, headers=headers, timeout=int(timeout)))
    except requests.exceptions.RequestException as e:
        return (False, {'error': e})


def _patch(url: str = None, headers: dict = None, data: dict = None, timeout: str = "10") -> tuple:
    """PATCH the information from provided url.

    :param url: The URL we want to PATCH.
    :type url: str
    :param headers: The headers.
    :type headers: dict
    :param data: The headers.
    :type data: dict
    :param timeout: The timeout in seconds
    :type timeout: str
    :rtype: tuple
    :return: Succes (or not) with the return object
    """
    if not url:
        raise ValueError('Please provide the URL.')
    if not headers:
        headers = {}
    if not data:
        data = {}
    try:
        return (True, requests.patch(url, headers=headers, data=data, timeout=int(timeout)))
    except requests.exceptions.RequestException as e:
        return (False, {'error': e})


def _post(url: str = None, headers: dict = None, data: dict = None, timeout: str = "10") -> tuple:
    """POST the information from provided url.

    :param url: The URL we want to POST.
    :type url: str
    :param headers: The headers.
    :type headers: dict
    :param data: The data we want to POST.
    :type data: dict
    :param timeout: The timeout in seconds
    :type timeout: str
    :rtype: tuple
    :return: Succes (or not) with the return object
    """
    if not url:
        raise ValueError('Please provide the URL.')
    if not headers:
        headers = {}
    try:
        return (True, requests.post(url, headers=headers, data=data, timeout=timeout))
    except requests.exceptions.RequestException as e:
        return (False, {'error': e})


def _put(url: str = None, headers: dict = None, timeout: str = "10") -> tuple:
    """PUT the information from provided url.

    :param url: The URL we want to PUT.
    :type url: str
    :param headers: The headers.
    :type headers: dict
    :param timeout: The timeout in seconds
    :type timeout: str
    :rtype: tuple
    :return: Succes (or not) with the return object
    """
    if not url:
        raise ValueError('Please provide the URL.')
    if not headers:
        headers = {}
    try:
        return (True, requests.put(url, headers=headers, timeout=int(timeout)))
    except requests.exceptions.RequestException as e:
        return (False, {'error': e})


def _delete(url: str = None, headers: dict = None, timeout: str = "10") -> tuple:
    """DELETE the information from provided url.

    :param url: The URL we want to DELETE.
    :type url: str
    :param headers: The headers.
    :type headers: dict
    :param timeout: The timeout in seconds
    :type timeout: str
    :rtype: tuple
    :return: Succes (or not) with the return object
    """
    if not url:
        raise ValueError('Please provide the URL.')
    if not headers:
        headers = {}
    try:
        return (True, requests.delete(url, headers=headers, timeout=int(timeout)))
    except requests.exceptions.RequestException as e:
        return (False, {'error': e})


def verifyResponse(success: bool = None, data: dict = None, debug: bool = False) -> dict:
    """Get the correct configuration for the repository.

    :param success: The default configuration we will override.
    :type success: bool
    :param data: The compleet requests data object.
    :type data: dict
    :param debug: If we need to debug or not.
    :type debug: bool
    :rtype: dict
    :return: The combination of the default and overriden config.
    """
    if success and data.ok:
        generic.debugLog(debug=debug, message="We have successful request, returning json data.")
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
