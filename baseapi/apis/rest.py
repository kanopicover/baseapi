import os
import requests

from ..exceptions import QueryException
from ..utils import remove_trailing_slash

from .api import Api


class RestApi(Api):
    IGNORED_ATTRIBUTES = Api.IGNORED_ATTRIBUTES | set([
        'get',
        'post',
        'put',
        'patch',
        'delete',
        'options',
        'perform_request',
    ])

    def get(self, path, data=None, headers=None):
        return self.perform_request('get', path, data=data, headers=headers)

    def post(self, path, data=None, headers=None):
        return self.perform_request('post', path, data=data, headers=headers)

    def put(self, path, data=None, headers=None):
        return self.perform_request('put', path, data=data, headers=headers)

    def patch(self, path, data=None, headers=None):
        return self.perform_request('patch', path, data=data, headers=headers)

    def delete(self, path, data=None, headers=None):
        return self.perform_request('delete', path, data=data, headers=headers)

    def options(self, path, data=None, headers=None):
        return self.perform_request('options', path, data=data, headers=headers)

    def perform_request(self, method, path, data=None, headers=None):
        url = remove_trailing_slash(self.client.url)
        url = f'{url}{path}'
        response = getattr(requests, method)(url, json=data, headers=headers)
        if response.status_code not in self.SUCCESS_RESPONSE_CODES:
            msg = response.content
            raise QueryException(f'API error: {msg}')
        response_data = response.json()
        return response_data
