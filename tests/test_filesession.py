import json
from pathlib import Path

from baseapi.client import Client
from baseapi.sessions import FileSession


def test_saves_jwt():
    client = Client(jwt='test')
    session = FileSession('/tmp/test.json')
    session.save(client)
    with open('/tmp/test.json') as f:
        data = json.loads(f.read())
    assert data == {'jwt': 'test'}


def test_loads_jwt():
    with open('/tmp/test.json', 'w') as f:
        f.write(json.dumps({'jwt': 'test'}))
    client = Client()
    session = FileSession('/tmp/test.json')
    session.load(client)
    assert client.jwt == 'test'


def test_deletes_jwt():
    with open('/tmp/test.json', 'w') as f:
        f.write(json.dumps({'jwt': 'test'}))
    client = Client()
    session = FileSession('/tmp/test.json')
    session.save(client)
    assert not Path('/tmp/test.json').exists()
