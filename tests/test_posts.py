from client import get_post

def test_get_post_success(valid_post_response):
    response = valid_post_response

    assert response.status_code == 200
    assert response.json()["id"] == 1



def test_get_post_not_found():
    response = get_post(999999)

    assert response.status_code == 404
