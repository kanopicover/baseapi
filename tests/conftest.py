from baseapi.client import Client

import pytest


@pytest.fixture
def client():
    yield Client(domain='http://server:8000')


@pytest.fixture
def auth_client():
    token = (
        'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
        '.eyJlbWFpbCI6InRlc3RpbmdAYnNlYy5tZSI'
        'sImV4cCI6MTU2MDgzMDY2OSwib3JpZ0lhdCI'
        '6MTU2MDgzMDM2OX0.B5FOv6qPqtLMCypOqFX'
        'VHDBuwaLnyRu2tAHOdZSAZfU'
    )
    yield Client(
        domain='http://server:8000',
        encrypt=False,
        jwt=token
    )
