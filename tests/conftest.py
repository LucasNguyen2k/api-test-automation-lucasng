import pytest
from client import get_post

@pytest.fixture
def valid_post_response():
    return get_post(1)
