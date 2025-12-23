import pytest
from client import get_post

@pytest.mark.parametrize(
    "post_id, expected_status",
    [
        (1, 200),
        (2, 200),
        (999999, 404),
    ],
)
def test_get_post_various_cases(post_id, expected_status):
    response = get_post(post_id)
    assert response.status_code == expected_status
