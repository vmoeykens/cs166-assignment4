"""
Basic tests for Flask app
"""

# pylint: disable=W0611,W0621

from flask.testing import FlaskClient
from tests.fixtures import client, app


def test_index(client: FlaskClient):
    """Index """
    response = client.get("/")
    assert response.status_code == 200
    assert b'Catamount Community Bank' in response.data
