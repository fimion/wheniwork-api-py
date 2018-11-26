"""
A Python Wrapper for WhenIWork.com
    .. moduleauthor:: Alex Riviere <fimion@gmail.com>
"""

import requests
from wheniwork.version import VERSION_NUMBER


def raise_for_status_with_message(resp):
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as error:
        if resp.text:
            raise requests.exceptions.HTTPError('{} \nError message: {}'.format(str(error), resp.text))
        else:
            raise error


class WhenIWork(object):
    """.. py:class: WhenIWork([:param token:=None, :param options:=dict()])
    :param token: The user WhenIWork API token
    :param options: Allows you to set the `headers` and the `endpoint` from a dict.

    Methods:

    """
    # Private Variables
    __api_token = None
    __api_endpoint = "https://api.wheniwork.com/2"
    __api_headers = {
        'user-agent': 'wheniwork-api-py/{version}'
        .format(version=VERSION_NUMBER)
    }
    __verify_ssl = False
    __api_resp = None

    def __init__(self, token=None, options=None):
        """
        .. py:method:: init
        Create a new instance.
        :param token: The user WhenIWork API token
        :param options: Allows you to set the `headers` and the `endpoint` from a dict.
        """
        self.__api_token = token

        if isinstance(options, dict):
            if 'headers' in options:
                self.__api_headers = options['headers']

            if 'endpoint' in options:
                self.__api_endpoint = options['endpoint']

    @property
    def token(self):
        """
        Used to set or retrieve the user's api token::

            from wheniwork import WhenIWork

            a = WhenIWork()
            a.token = "ilovemyboss"
            print(a.token)
        """
        return self.__api_token

    @token.setter
    def token(self, token):
        """
        """
        self.__api_token = token

    @property
    def endpoint(self):
        """
        Used to set or retrieve the api endpoint::

            from wheniwork import WhenIWork

            a = WhenIWork()
            a.endpoint = "https://api.wheniwork.com/2"
            print(a.endpoint)
        """
        return self.__api_endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """

        :param endpoint:
        :return:
        """
        self.__api_endpoint = endpoint

    @property
    def headers(self):
        """
        Used to set or retrieve the api endpoint::

            from wheniwork import WhenIWork

            a = WhenIWork()
            a.headers = {W-Key:"iworksoharditsnotfunny"}
            print(a.headers['W-Key'])
        """
        return self.__api_headers

    @headers.setter
    def headers(self, headers):
        """

        :param headers:
        :return:
        """
        self.__api_headers = headers

    @property
    def resp(self):
        """
        Used to get the last API Response Data::

            from wheniwork import WhenIWork

            a = WhenIWork(token="iworksomuchitsnotfunny")
            a.get("/locations")
            print(a.resp)

        Note: This is a read only variable.
        """
        return self.__api_resp

    def login(self, username, password, key):
        """
        Sets the user API token, and returns a dictionary of user information.

        :param username: The email for the user account.
        :param password: The password for the user account.
        :param key: the developer key given to you by WhenIWork.com
        :return dict:

        """

        url = self.endpoint+"/login"
        params = {'username': username, 'password': password}
        head = {'W-Key': key}
        head.update(self.headers)
        resp = requests.post(url, json=params, headers=head)
        raise_for_status_with_message(resp)
        self.__api_resp = resp.json()
        data = self.resp
        if 'login' in data and 'token' in data['login']:
            self.token = data['login']['token']
        return data

    def get(self, method, params=None, headers=None):
        """
        Send a get request to the WhenIWork api

        :param method: The API method to call, e.g. '/users'
        :param params: a dictionary of arguments to pass the method
        :param headers: a dictionary of custom headers to be passed.
        :return: a dictionary of the decoded json API response.

        """
        if isinstance(method, str):
            if self.token is not None:
                url = self.endpoint+method
                head = {'W-Token': self.token}
                head.update(self.headers)
                if headers:
                    head.update(headers)
                resp = requests.get(url, params, headers=head)
                raise_for_status_with_message(resp)
                self.__api_resp = resp.json()
                return self.resp
            else:
                return {'error': 'Token is not set!!'}
        else:
            return {'error': 'Method is not str!!'}

    def post(self, method, params=None, headers=None):
        """
        POST to the WhenIWork api

        :param method: The API method to call, e.g. '/users'
        :param params: a dictionary of arguments to pass the method
        :param headers: a dictionary of custom headers to be passed.
        :return: a dictionary of the decoded json API response.
        """
        if isinstance(method, str):
            if self.token is not None:
                url = self.endpoint+method
                head = {'W-Token': self.token}
                head.update(self.headers)
                if headers:
                    head.update(headers)
                resp = requests.post(url, json=params, headers=head)
                raise_for_status_with_message(resp)
                self.__api_resp = resp.json()
                return self.resp
            else:
                return {'error': 'Token is not set!!'}
        else:
            return {'error': 'Method is not str!!'}

    def create(self, method, params=None, headers=None):
        """
        Synonym of post

        :param method:
        :param params:
        :param headers:
        :return:
        """
        return self.post(method, params=params, headers=headers)

    def update(self, method, params=None, headers=None):
        """
        Update an object on WhenIWork

        :param method: The API method to call, e.g. '/users/1' MUST INCLUDE ID OF OBJECT.
        :param params: a dictionary of arguments to pass the method
        :param headers: a dictionary of custom headers to be passed.
        :return: a dictionary of the decoded json API response.
        """
        if isinstance(method, str):
            if self.token is not None:
                url = self.endpoint+method
                head = {'W-Token': self.token}
                head.update(self.headers)
                if headers:
                    head.update(headers)
                resp = requests.put(url, json=params, headers=head)
                raise_for_status_with_message(resp)
                self.__api_resp = resp.json()
                return self.resp
            else:
                return {'error': 'Token is not set!!'}
        else:
            return {'error': 'Method is not str!!'}

    def delete(self, method, headers=None):
        """
                Delete an object on WhenIWork

                :param method: The API method to call, e.g. '/users/1' MUST INCLUDE ID OF OBJECT.
                :param headers: a dictionary of custom headers to be passed.
                :return: a dictionary of the decoded json API response.
                """
        if isinstance(method, str):
            if self.token is not None:
                url = self.endpoint + method
                head = {'W-Token': self.token}
                head.update(self.headers)
                if headers:
                    head.update(headers)
                resp = requests.delete(url, headers=head)
                raise_for_status_with_message(resp)
                self.__api_resp = resp.json()
                return self.resp
            else:
                return {'error': 'Token is not set!!'}
        else:
            return {'error': 'Method is not str!!'}
