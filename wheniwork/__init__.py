"""
.. module:: WhenIWork
    :synopsis: A Python Wrapper for WhenIWork.com

.. moduleauthor:: Alex Riviere <fimion@gmail.com>
"""

import requests


class WhenIWork(object):
    """
    .. class:: WhenIWork
    """
    # Library Version
    version = 0.1

    # Private Variables
    __api_token = None
    __api_endpoint = "https://wheniwork.com/2"
    __api_headers = None
    __verify_ssl = False

    def __init__(self, token=None, options=dict()):
        """
        Create a new instance.
        :param token: The user WhenIWork API token
        :param options: Allows you to set the `headers` and the `endpoint` from a dict.
        """
        self.__api_token = token

        if 'headers' in options:
            self.__api_headers = options['headers']

        if 'endpoint' in options:
            self.__api_endpoint = options['endpoint']

    @property
    def token(self):
        """
        Gets the current token
        :return str: the user WhenIWork api token
        """
        return self.__api_token

    @token.setter
    def token(self, token):
        """
        Sets the token.
        :param token:
        :return WhenIWork:
        """
        self.__api_token = token
        return self
