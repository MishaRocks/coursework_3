import pytest

from app.api.utils import api_posts

from app.run import app


def test_api_posts():

    response = app.test_client().get('/api')
    assert response.status_code == 200

